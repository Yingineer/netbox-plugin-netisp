from django.urls import path
from django.http import HttpResponse

from .views import *
from .netbox_netisp.views.generic import HomeView

app_name = 'netbox_netisp'

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("customers/", CustomerListView.as_view(), name="customer_list"),
    path("customers/add", CustomerEditView.as_view(), name="customer_add"),
    path("customers/<int:pk>/edit/>", CustomerEditView.as_view(), name="customer_edit")
]