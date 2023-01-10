from django.urls import path

from . import views

app_name = "contracts"

urlpatterns = [
    path(
        "managers_dashboard",
        views.ManagersDashboard.as_view(),
        name="managers_dashboard",
    ),
    path("all_contracts", views.ContractListView.as_view(), name="all_contracts"),
    path(
        "directors_approval_list",
        views.DirectorsApprovalList.as_view(),
        name="directors_approval_list",
    ),
    path(
        "directors_approval_detail/<pk>",
        views.DirectorsApprovalDetail.as_view(),
        name="directors_approval_detail",
    ),
    path(
        "out_of_contract_list",
        views.OutOfContractList.as_view(),
        name="out_of_contract_list",
    ),
]
