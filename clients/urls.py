from django.urls import path

from . import views

app_name = "clients"

urlpatterns = [
    path(
        "client_contracts/<pk>",
        views.ClientDetailView.as_view(),
        name="client_contracts",
    ),
    path(
        "contract_detail/<pk>",
        views.ContractDetailView.as_view(),
        name="contract_detail",
    ),
    path("pdf/<pk>", views.contracts_render_pdf_view, name="contract_pdf_view"),
    # path("meter_reading/<pk>", views.meter_reading, name="meter_reading"),
    path("meter_reading/<pk>", views.meter_reading, name='meter_reading'),
]
