from django.shortcuts import render
from rest_framework import viewsets, request
from rest_framework.response import Response
from api.models import Project
from api.serializer import ProjectSerializer,ProjectDetailSerializer

# Create your views here.
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer
    lookup_field = 'slug'
    context={'request': request}

    def list(self, request, *args, **kwargs):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)