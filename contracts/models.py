from datetime import date

from django.db import models
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords

from account_managers.models import AccountManager
from client_managers.models import ClientManager
from clients.models import Client
from core.models import TimeStampedModel
from utilities.models import Supplier, Utility


class ContractsManager(models.Manager):
    def get_queryset(self):
        return (
            super(ContractsManager, self)
            .get_queryset()
            .select_related("client", "supplier", "utility")
        )


class Contract(TimeStampedModel):
    seamless = models.BooleanField(default=False)
    non_seamless = models.BooleanField(default=False)
    dwellent_id = models.CharField(max_length=100, null=True, blank=True)
    bid_id = models.CharField(max_length=100, null=True, blank=True)
    property_reference = models.CharField(max_length=100, null=True, blank=True)
    portal_status = models.CharField(max_length=255, null=True, blank=True)
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name="client_contracts"
    )

    is_directors_approval = models.BooleanField(default=False)
    under_objection = models.BooleanField(default=False)
    business_name = models.CharField(max_length=255)
    company_reg_number = models.CharField(max_length=100, null=True, blank=True)
    utility = models.ForeignKey(
        Utility, on_delete=models.CASCADE, related_name="contract_utilities"
    )
    top_line = models.CharField(max_length=40, null=True, blank=True)
    mpan_mpr = models.CharField(max_length=255)
    meter_serial_number = models.CharField(max_length=100, null=True, blank=True)
    building_name = models.CharField(max_length=255, null=True, blank=True)
    site_address = models.TextField()
    billing_address = models.CharField(max_length=255, null=True, blank=True)
    supplier = models.ForeignKey(
        Supplier, on_delete=models.CASCADE, related_name="contract_suppliers"
    )
    contract_start_date = models.DateField(null=True, blank=True)
    contract_end_date = models.DateField(null=True, blank=True)
    account_number = models.CharField(max_length=100, null=True, blank=True)

    eac = models.CharField(max_length=100, null=True, blank=True)
    day_consumption = models.CharField(max_length=20, null=True, blank=True)
    night_consumption = models.CharField(max_length=20, null=True, blank=True)
    vat = models.CharField(max_length=25, null=True, blank=True)
    contract_value = models.DecimalField(
        max_digits=9, decimal_places=2, null=True, blank=True
    )
    standing_charge = models.CharField(max_length=50, null=True, blank=True)
    sc_frequency = models.CharField(max_length=250, null=True, blank=True)
    unit_rate_1 = models.CharField(max_length=25, null=True, blank=True)
    unit_rate_2 = models.CharField(max_length=25, null=True, blank=True)
    unit_rate_3 = models.CharField(max_length=25, null=True, blank=True)
    feed_in_tariff = models.CharField(max_length=20, null=True, blank=True)
    seamless_status = models.CharField(max_length=25, null=True, blank=True)
    profile = models.CharField(max_length=100, null=True, blank=True)
    is_ooc = models.BooleanField(default=False)
    service_type = models.CharField(max_length=50, null=True, blank=True)

    pence_per_kilowatt = models.CharField(max_length=12, null=True, blank=True)
    day_kilowatt_hour_rate = models.CharField(max_length=12, null=True, blank=True)
    night_rate = models.CharField(max_length=10, null=True, blank=True)
    annualised_budget = models.CharField(max_length=100, null=True, blank=True)
    commission_per_annum = models.CharField(max_length=100, null=True, blank=True)
    commission_per_unit = models.CharField(max_length=100, null=True, blank=True)
    commission_per_contract = models.CharField(max_length=100, null=True, blank=True)
    partner_commission = models.CharField(max_length=100, null=True, blank=True)
    smart_meter = models.CharField(max_length=25, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    kva = models.CharField(max_length=15, null=True, blank=True)
    future_contract_start_date = models.DateField(null=True, blank=True)
    future_unit_rate_1 = models.CharField(max_length=25, null=True, blank=True)
    future_unit_rate_2 = models.CharField(max_length=25, null=True, blank=True)
    future_unit_rate_3 = models.CharField(max_length=25, null=True, blank=True)
    history = HistoricalRecords()

    class Meta:
        indexes = [
            models.Index(fields=["mpan_mpr"]),
            models.Index(fields=["client"]),
            models.Index(fields=["-client"]),
            models.Index(fields=["business_name"]),
            models.Index(fields=["-business_name"]),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=["mpan_mpr", "id"],
                name="unique_contract",
            )
        ]
        verbose_name = _("Client Contract")
        verbose_name_plural = _("Client Contracts")
        ordering = ["id"]

    objects = ContractsManager()

    def __str__(self):
        return self.business_name

    @property
    def Days_till(self):
        today = date.today()
        days_till = self.contract_end_date - today
        days_till_stripped = str(days_till).split(",", 1)[0]
        return days_till_stripped
