from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic import DetailView, ListView

from contracts.models import Contract
from core.decorators import client_manager_required
from core.views import HTMLTitleMixin

User = get_user_model()


@method_decorator([never_cache, client_manager_required], name="dispatch")
class ClientManagerDashBoard(LoginRequiredMixin, HTMLTitleMixin, ListView):
    model = Contract
    template_name = "client_managers/dashboard.html"
    html_title = "Contracts List"
    login_url = "/users/login/"

    # def get_html_title(self):
    #     return self.object.business_name

    def get_queryset(self, *args, **kwargs):
        return (
            super(ClientManagerDashBoard, self)
            .get_queryset(*args, **kwargs)
            .filter(client__client_manager__client_manager=self.request.user)
        )


@method_decorator([never_cache, client_manager_required], name="dispatch")
class ClientManagerContractDetail(LoginRequiredMixin, HTMLTitleMixin, DetailView):
    model = Contract
    template_name = "client_managers/contract_detail.html"
    login_url = "/users/login/"

    def get_html_title(self):
        return self.object.business_name

    def get_queryset(self, *args, **kwargs):
        return (
            super(ClientManagerContractDetail, self)
            .get_queryset(*args, **kwargs)
            .filter(client__client_manager__client_manager=self.request.user)
        )
