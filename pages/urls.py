from django.urls import path

from . import views

# from django.views.generic import TemplateView


app_name = "pages"

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("market_update", views.MarketUpdateView.as_view(), name="market_update"),
    path(
        "seamless_utilities",
        views.SeamlessUtilitiesView.as_view(),
        name="seamless_utilities",
    ),
    path("our_partners", views.PartnersView.as_view(), name="partners"),
    path("our_services", views.OurServicesView.as_view(), name="our_services"),
    path("contact_us", views.contact_us, name="contact_us"),
    path(
        "complaints_policy",
        views.ComplaintsPolicyView.as_view(),
        name="complaints_policy",
    ),
    path("privacy_policy", views.PrivacyPolicyView.as_view(), name="privacy_policy"),
]
