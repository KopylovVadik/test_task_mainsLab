from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=200, null=False, primary_key=True)


class Organization(models.Model):
    client_name = models.ForeignKey(Client, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=False, primary_key=True)


class Bills(models.Model):
    client_org = models.ForeignKey(Organization, null=True, on_delete=models.CASCADE)
    number = models.IntegerField(null=True)
    sum = models.FloatField(null=True)
    date = models.DateField(null=True)
