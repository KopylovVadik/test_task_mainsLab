from rest_framework import serializers
from rest_framework.fields import FileField
from rest_framework.serializers import ModelSerializer, Serializer

from backend.models import Client, Bills, Organization


class ClientSerializer(ModelSerializer):
    organization_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Client
        fields = '__all__'


class OrganizationSerializer(ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


class BillsSerializer(ModelSerializer):
    class Meta:
        model = Bills
        fields = '__all__'


class UploadSerializer(Serializer):
    file_uploaded = FileField()

    class Meta:
        fields = ['file_uploaded']
