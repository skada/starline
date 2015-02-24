from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from resources.models import Resource
from resources.serializers import ResourceSerializer


class ResourceView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get_object(self, pk):
        try:
            return Resource.objects.get(pk=pk)
        except Resource.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        resource = self.get_object(pk)
        serializer = ResourceSerializer(resource,)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
            resource = self.get_object(pk)
            serializer = ResourceSerializer(resource, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
