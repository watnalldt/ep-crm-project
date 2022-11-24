from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import get_template
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic import DetailView
from xhtml2pdf import pisa

from clients.forms import MeterForm
from contracts.models import Contract
from core.views import HTMLTitleMixin

from .models import Client


@method_decorator([never_cache], name="dispatch")
class ClientDetailView(LoginRequiredMixin, HTMLTitleMixin, DetailView):
    """Details all contracts for that client"""

    model = Client
    template_name = "clients/contracts/client_detail.html"
    login_url = "/users/login/"

    def get_html_title(self):
        return self.object.client

    def get_queryset(self):
        return Client.objects.filter(account_manager__account_manager=self.request.user)

    # def get_queryset(self, *args, **kwargs):
    #     return (
    #         super(ClientDetailView, self)
    #         .get_queryset(*args, **kwargs)
    #         .filter(account_manager__account_manager=self.request.user)
    #     )


@method_decorator([never_cache], name="dispatch")
class ContractDetailView(LoginRequiredMixin, HTMLTitleMixin, DetailView):
    model = Contract
    template_name = "clients/contracts/contract_detail.html"
    login_url = "/users/login/"

    def get_html_title(self):
        return self.object.business_name

    def get_queryset(self):
        return Contract.objects.filter(
            client__account_manager__account_manager=self.request.user
        )

    # def get_queryset(self, *args, **kwargs):
    #     return (
    #         super(ContractDetailView, self)
    #         .get_queryset(*args, **kwargs)
    #         .filter(client__account_manager__account_manager=self.request.user)
    #     )


@login_required(login_url="/users/login/")
def contracts_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get("pk")
    contract = get_object_or_404(
        Contract, pk=pk, client__account_manager__account_manager=request.user.id
    )

    template_path = "contracts/generate_pdf.html"
    context = {"contract": contract}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type="application/pdf")

    # to directly download the pdf we need attachment
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    # to view on browser we can remove attachment
    response["Content-Disposition"] = 'filename="report.pdf"'

    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response)
    # if error then show some error view
    if pisa_status.err:
        return HttpResponse("We had some errors <pre>" + html + "</pre>")
    return response


def meter_reading(request, *args, **kwargs):
    pk = kwargs.get("pk")
    contract = get_object_or_404(
        Contract, pk=pk, client__client_manager__client_manager=request.user.id
    )

    if request.method == "POST":
        form = MeterForm(request.POST, request.FILES)

        if form.is_valid():
            subject = "Meter Reading"
            data = {
                "from_email": form.cleaned_data["from_email"],
                "client_name": form.cleaned_data["client_name"],
                "site_address": form.cleaned_data["site_address"],
                "mpan_mpr": form.cleaned_data["mpan_mpr"],
                "meter_serial_number": form.cleaned_data["meter_serial_number"],
                "utility_type": form.cleaned_data["utility_type"],
                "supplier": form.cleaned_data["supplier"],
                "meter_read": form.cleaned_data["meter_read"],
                "meter_reading_date": form.cleaned_data["meter_reading_date"],
            }

            message = "\n".join(data.values())

            try:
                send_mail(
                    subject,
                    message,
                    "josh@eneryportdolio.co.uk",
                    ["josh@energyportfolio.co.uk"],
                )
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("pages:home")
    form = MeterForm(
        initial={
            "from_email": request.user.email,
            "client_name": contract.client,
            "site_address": contract.site_address,
            "mpan_mpr": contract.mpan_mpr,
            "meter_serial_number": contract.meter_serial_number,
            "utility_type": contract.utility,
            "supplier": contract.supplier,
        }
    )
    return render(
        request,
        "client_managers/meter_reading.html",
        {"form": form, "contract": contract},
    )
