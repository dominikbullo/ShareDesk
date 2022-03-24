from django_filters import rest_framework as django_filters

from rest_framework import viewsets, filters, pagination
from rest_framework.settings import api_settings

from apps.teams.api.serializers import TeamSerializer
from apps.teams.models import Team


# https://www.sankalpjonna.com/learn-django/pagination-made-easy-with-django-rest-framework
class TeamViewSetPagination(pagination.PageNumberPagination):
    page_size = 100
    page_size_query_param = 'perPage'
    page_query_param = 'page'


class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
    pagination_class = TeamViewSetPagination
    filter_backends = api_settings.DEFAULT_FILTER_BACKENDS + [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = '__all__'
    filterset_fields = "__all__"
    search_fields = ["name"]
