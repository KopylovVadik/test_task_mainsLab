from django.urls import path

from .views import UploadOrg, UploadBills, GetClients, GetListBills

app_name = "backend"

urlpatterns = [
    path("api/upload_org", UploadOrg.as_view(), name="upload_org"),
    path("api/upload_bills", UploadBills.as_view(), name="upload_bills"),
    path("api/get_clients", GetClients.as_view(), name="get_clients"),
    path("api/get_bills", GetListBills.as_view(), name="get_bills"),

]

