import logging

import openpyxl
from django.db.models import Count
from rest_framework import generics
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from . import models
from .models import Client, Bills, Organization
from .serializers import UploadSerializer, ClientSerializer, BillsSerializer

logger = logging.getLogger('django')


class UploadOrg(APIView):
    serializer_class = UploadSerializer

    def post(self, request):

        file_uploaded = request.FILES.get('file_uploaded')

        workbook = openpyxl.load_workbook(file_uploaded)
        worksheet_client = workbook.worksheets[0].values
        worksheet_organization = workbook.worksheets[1].values

        for index, value in enumerate(worksheet_client):
            if index == 0:
                continue

            try:
                client = models.Client(
                    name=value[0]
                ).save()
            except Exception as e:
                logger.error(e)

        for index, value in enumerate(worksheet_organization):
            if index == 0:
                continue

            try:
                organization = models.Organization(
                    client_name=Client.objects.get(name=value[0]),
                    name=value[1]
                ).save()
            except Exception as e:
                logger.error(e)

        return Response(status=201)


class UploadBills(APIView):
    serializer_class = UploadSerializer

    def post(self, request):
        file_uploaded = request.FILES.get('file_uploaded')

        workbook = openpyxl.load_workbook(file_uploaded)
        worksheet_bills = workbook.active

        for index, value in enumerate(worksheet_bills):
            if index == 0:
                continue
            try:
                bills = models.Bills(
                    client_org=Organization.objects.get(name=value[0].value),
                    number=value[1].value,
                    sum=value[2].value,
                    date=value[3].value
                ).save()
            except Exception as e:
                logger.error(e)

        return Response(status=201)


class GetClients(ListAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.annotate(organization_count=Count('organization'))


class GetListBills(generics.ListAPIView):
    serializer_class = BillsSerializer
    queryset = Bills.objects.all()
    filterset_fields = ['client_org']
