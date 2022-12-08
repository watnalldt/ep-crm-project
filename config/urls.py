"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.views import defaults as default_views

from core import views

admin.site.site_header = "Energy Portfolio Contract Management"
admin.site.site_title = "Energy Portfolio CRM Portal"
admin.site.index_title = "Energy Portfolio Contract Management"


urlpatterns = [
    path("grappelli/", include("grappelli.urls")),  # grappelli URLS
    path("ep_crm_portal/", admin.site.urls),
    path("", include("pages.urls")),
    path("users/", include("users.urls")),
    path("account_managers/", include("account_managers.urls")),
    path("client_managers/", include("client_managers.urls")),
    path("clients/", include("clients.urls")),
    path("contracts/", include("contracts.urls")),
    # Password Management
    path("password_reset", views.password_reset_request, name="password_reset"),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="passwords/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="passwords/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]
if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]

    if settings.DEBUG:
        urlpatterns += [
            path("__reload__/", include("django_browser_reload.urls")),
        ]

    # Enable the debug toolbar only in DEBUG mode.
    if settings.DEBUG and settings.DEBUG_TOOLBAR:
        urlpatterns = [
            path("__debug__/", (include("debug_toolbar.urls")))
        ] + urlpatterns
