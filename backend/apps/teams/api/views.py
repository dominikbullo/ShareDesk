from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from apps.teams.api.serializers import TeamSerializer
from apps.teams.models import Team


class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
