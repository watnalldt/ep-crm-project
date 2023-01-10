from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic import DetailView, ListView

from .models import Objection


@method_decorator([never_cache], name="dispatch")
class OutstandingObjectionsList(LoginRequiredMixin, UserPassesTestMixin, ListView):
    # Out Of Contract Lis
    model = Objection
    template_name = "objections/outstanding_objections_list.html"
    queryset = Objection.objects.filter(objection_status="OUTSTANDING")
    context_object_name = "objections"
    login_url = "/users/login/"

    def test_func(self):
        return self.request.user.groups.filter(name="Managers").exists()


class ObjectionsOutstandingDetail(UserPassesTestMixin, DetailView):
    model = Objection
    template_name = "objections/objections_outstanding_detail.html"
    login_url = "/users/login/"

    def test_func(self):
        return self.request.user.groups.filter(name="Managers").exists()


@method_decorator([never_cache], name="dispatch")
class PendingObjectionsList(LoginRequiredMixin, UserPassesTestMixin, ListView):
    # Out Of Contract Lis
    model = Objection
    template_name = "objections/objections_pending_list.html"
    queryset = Objection.objects.filter(objection_status="PENDING")
    context_object_name = "objections"
    login_url = "/users/login/"

    def test_func(self):
        return self.request.user.groups.filter(name="Managers").exists()


class ObjectionsPendingDetail(UserPassesTestMixin, DetailView):
    model = Objection
    template_name = "objections/objections_pending_detail.html"
    login_url = "/users/login/"

    def test_func(self):
        return self.request.user.groups.filter(name="Managers").exists()
