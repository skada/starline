from resources.models import ResourceBase

__author__ = 'jakubskaryd'

from rest_framework import serializers


class ResourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResourceBase
        fields = ('name', 'left', 'top',)
