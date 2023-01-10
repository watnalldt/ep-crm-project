from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic import DetailView, ListView, TemplateView

from .models import Contract


@method_decorator([never_cache], name="dispatch")
class ManagersDashboard(LoginRequiredMixin, UserPassesTestMixin, TemplateView):  # noqa
    template_name = "partials/dashboards/managers_dashboard.html"
    login_url = "/users/login/"

    def is_member(self):

        return self.request.user.groups.filter(name="Managers").exists()


@method_decorator([never_cache], name="dispatch")
class ContractListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Contract
    template_name = "contracts/all_contracts.html"
    context_object_name = "contracts"
    login_url = "/users/login/"

    def test_func(self):
        return self.request.user.groups.filter(name="Managers").exists()


method_decorator([never_cache], name="dispatch")


class DirectorsApprovalList(UserPassesTestMixin, ListView):
    # Directors Approval List
    model = Contract
    template_name = "contracts/directors_approval_list.html"
    queryset = Contract.objects.filter(is_directors_approval=True)
    context_object_name = "contracts"
    login_url = "/users/login/"

    def test_func(self):
        return self.request.user.groups.filter(name="Managers").exists()


class DirectorsApprovalDetail(UserPassesTestMixin, DetailView):
    model = Contract
    template_name = "contracts/directors_approval_detail.html"
    login_url = "/users/login/"

    def test_func(self):
        return self.request.user.groups.filter(name="Managers").exists()


class OutOfContractList(UserPassesTestMixin, ListView):
    # Directors Approval List
    model = Contract
    template_name = "contracts/out_of_contract_list.html"
    queryset = Contract.objects.filter(is_ooc=True)
    context_object_name = "contracts"
    login_url = "/users/login/"

    def test_func(self):
        return self.request.user.groups.filter(name="Managers").exists()
