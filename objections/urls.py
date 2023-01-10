from django.urls import path

from . import views

app_name = "objections"

urlpatterns = [
    path(
        "objections_outstanding",
        views.OutstandingObjectionsList.as_view(),
        name="objections_outstanding",
    ),
    path(
        "objections_outstanding_detail/<pk>",
        views.ObjectionsOutstandingDetail.as_view(),
        name="objections_outstanding_detail",
    ),
    path(
        "objections_pending",
        views.PendingObjectionsList.as_view(),
        name="objections_pending",
    ),
    path(
        "objections_pending_detail/<pk>",
        views.ObjectionsPendingDetail.as_view(),
        name="objections_pending_detail",
    ),
]
