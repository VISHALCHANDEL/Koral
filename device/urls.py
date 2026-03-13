from django.urls import path
from .views import dashboard,download_qr

urlpatterns = [
    path("", dashboard, name="dashboard"),
     path("download-qr/", download_qr, name="download_qr"),
]