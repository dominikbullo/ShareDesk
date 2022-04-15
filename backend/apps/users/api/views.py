from uuid import uuid4

import django_filters
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

from rest_framework import viewsets, filters, pagination, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from apps.teams.models import Team
from apps.users.models import User
from apps.users.api.serializers import UserSerializer, UserWriteSerializer


class UsersFilter(django_filters.FilterSet):
    # FIXME: multiple teams
    # https://devdreamz.com/question/951148-negation-or-exclude-filter-in-django-rest-framework
    teams__not = room = django_filters.ModelChoiceFilter(
        label='Teams (excluded)',
        empty_label='Excluded teams',
        queryset=Team.objects.all(),
        method='filter_team',
    )

    def filter_team(self, queryset, name, value):
        return queryset.exclude(teams=value.id)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "role", "teams", "teams__not", "is_active"]


# https://www.sankalpjonna.com/learn-django/pagination-made-easy-with-django-rest-framework
class UserViewSetPagination(pagination.PageNumberPagination):
    page_size = 100
    page_size_query_param = 'perPage'
    page_query_param = 'page'


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = UserViewSetPagination
    filterset_class = UsersFilter
    filter_backends = api_settings.DEFAULT_FILTER_BACKENDS + [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ["email", "first_name", "last_name", "role"]
    search_fields = ["email", "first_name", "last_name", "role"]
    permission_classes = []

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return UserSerializer
        return UserWriteSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(self.request.data.get('password'))
        user.save()

    def perform_update(self, serializer):
        user = serializer.save()
        if 'password' in self.request.data:
            user.set_password(self.request.data.get('password'))
            user.save()

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

    @action(methods=['GET'], detail=False)
    def profile(self, request):
        if request.user.is_authenticated:
            serializer = self.serializer_class(request.user)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    @action(methods=['POST'], detail=False)
    def login(self, request, format=None):
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        user = authenticate(username=email, password=password)

        if user:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    @action(methods=['POST'], detail=False)
    def register(self, request):
        email = request.data.get('email', None)

        if User.objects.filter(email__iexact=email).exists():
            return Response({'email': "User with this email address already exist"}, status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['POST'], detail=False)
    def password_reset(self, request, format=None):
        if User.objects.filter(email=request.data['email']).exists():
            user = User.objects.get(email=request.data['email'])
            params = {'user': user, 'DOMAIN': settings.DOMAIN}
            send_mail(
                subject='Password reset',
                message=render_to_string('mail/password_reset.txt', params),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[request.data['email']],
            )
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @action(methods=['POST'], detail=False)
    def password_change(self, request, format=None):
        if User.objects.filter(token=request.data['token']).exists():
            user = User.objects.get(token=request.data['token'])
            user.set_password(request.data['password'])
            user.token = uuid4()
            user.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            # Also, logout from Django itself and DRF
            logout(request)

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
