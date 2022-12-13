from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.views.generic import TemplateView

from core.views import HTMLTitleMixin

from .forms import ContactForm


class HomePageView(HTMLTitleMixin, TemplateView):
    template_name = "pages/index.html"
    html_title = "Energy Portfolio"


class MarketUpdateView(HTMLTitleMixin, TemplateView):
    template_name = "pages/market_update.html"
    html_title = "Energy Portfolio Market Update"


class SeamlessUtilitiesView(HTMLTitleMixin, TemplateView):
    template_name = "pages/seamless_utilities.html"
    html_title = "Energy Portfolio Seamless Utilities"


class PartnersView(HTMLTitleMixin, TemplateView):
    template_name = "pages/our_partners.html"
    html_title = "Energy Portfolio Our Partners"


class OurServicesView(HTMLTitleMixin, TemplateView):
    template_name = "pages/our_services.html"
    html_title = "Energy Portfolio Services"


def contact_us(request):
    template = "pages/contact_us.html"
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            contact_email = form.cleaned_data["contact_email"]
            company = form.cleaned_data["company"]
            message = form.cleaned_data["message"]

            html = render_to_string(
                "pages/contact_template.html",
                {
                    "first_name": first_name,
                    "last_name": last_name,
                    "contact_email": contact_email,
                    "company": company,
                    "message": message,
                },
            )

            send_mail(
                "New Contact Form Submission",
                "This is the message",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[
                    "david@energyportfolio.co.uk",
                ],
                html_message=html,
            )
            messages.success(request, "We will be in touch with you shortly.")
            return redirect("pages:home")
    else:
        form = ContactForm()

    return render(request, template, {"form": form})


class ComplaintsPolicyView(HTMLTitleMixin, TemplateView):
    template_name = "pages/complaints_policy.html"
    html_title = "EP Complaints Policy"


class PrivacyPolicyView(HTMLTitleMixin, TemplateView):
    template_name = "pages/privacy_policy.html"
    html_title = "EP Privacy Policy"
