from django.urls import path

from . import views

app_name = "client_managers"

urlpatterns = [
    path("dashboard/", views.ClientManagerDashBoard.as_view(), name="dashboard"),
    path(
        "contract_detail/<pk>",
        views.ClientManagerContractDetail.as_view(),
        name="contract_detail",
    ),
]
