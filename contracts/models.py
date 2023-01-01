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
    seamless = models.BooleanField(verbose_name="Seamless Contract", default=False)
    non_seamless = models.BooleanField(
        verbose_name="Non Seamless Contract", default=False
    )
    dwellent_id = models.CharField(
        verbose_name="Dwellent ID", max_length=100, null=True, blank=True
    )
    bid_id = models.CharField(
        verbose_name="BID ID", max_length=100, null=True, blank=True
    )
    property_reference = models.CharField(
        verbose_name="Property Reference", max_length=100, null=True, blank=True
    )
    portal_status = models.CharField(
        verbose_name="Portal Status", max_length=255, null=True, blank=True
    )
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        verbose_name="Client Name",
        related_name="client_contracts",
    )

    is_directors_approval = models.BooleanField(default=False)
    business_name = models.CharField(verbose_name="Business Name", max_length=255)
    company_reg_number = models.CharField(
        verbose_name="Company Reg Number", max_length=100, null=True, blank=True
    )
    utility = models.ForeignKey(
        Utility,
        on_delete=models.CASCADE,
        verbose_name="Utility Type",
        related_name="contract_utilities",
    )
    top_line = models.CharField(
        verbose_name="Top Line", max_length=40, null=True, blank=True
    )
    mpan_mpr = models.CharField(verbose_name="MPAN/MPR", max_length=255)
    meter_serial_number = models.CharField(max_length=100, null=True, blank=True)
    building_name = models.CharField(
        verbose_name="Building Name", max_length=255, null=True, blank=True
    )
    site_address = models.TextField(
        verbose_name="Site Address",
    )
    billing_address = models.CharField(
        verbose_name="Billing Address", max_length=255, null=True, blank=True
    )
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        verbose_name="Supplier Name",
        related_name="contract_suppliers",
    )
    contract_start_date = models.DateField(
        verbose_name="Contract Start Date", null=True, blank=True
    )
    contract_end_date = models.DateField(
        verbose_name="Contract End Date", null=True, blank=True
    )
    account_number = models.CharField(
        verbose_name="Account Number", max_length=100, null=True, blank=True
    )

    eac = models.FloatField(verbose_name="EAC", null=True, blank=True)
    day_consumption = models.FloatField(
        verbose_name="Day Consumption", null=True, blank=True
    )
    night_consumption = models.FloatField(
        verbose_name="Night Consumption", null=True, blank=True
    )
    vat = models.CharField(verbose_name="VAT", max_length=25, null=True, blank=True)
    contract_value = models.DecimalField(
        verbose_name="Contract Value",
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
    standing_charge = models.DecimalField(
        verbose_name="Standing Charge",
        max_digits=8,
        decimal_places=4,
        null=True,
        blank=True,
    )
    sc_frequency = models.CharField(
        verbose_name="Standing Charge Frequency", max_length=250, null=True, blank=True
    )
    unit_rate_1 = models.DecimalField(
        verbose_name="Unit Rate 1",
        max_digits=8,
        decimal_places=4,
        null=True,
        blank=True,
    )
    unit_rate_2 = models.DecimalField(
        verbose_name="Unit Rate 2",
        max_digits=8,
        decimal_places=4,
        null=True,
        blank=True,
    )
    unit_rate_3 = models.DecimalField(
        verbose_name="Unit Rate 3",
        max_digits=8,
        decimal_places=4,
        null=True,
        blank=True,
    )
    feed_in_tariff = models.DecimalField(
        verbose_name="Feed In Tariff",
        max_digits=8,
        decimal_places=4,
        null=True,
        blank=True,
    )
    seamless_status = models.CharField(
        verbose_name="Seamless Status", max_length=25, null=True, blank=True
    )
    profile = models.CharField(
        verbose_name="Profile", max_length=100, null=True, blank=True
    )
    is_ooc = models.BooleanField(verbose_name="Out Of Contract", default=False)
    service_type = models.CharField(max_length=50, null=True, blank=True)

    pence_per_kilowatt = models.DecimalField(
        verbose_name="Pence Per Kilowatt",
        max_digits=8,
        decimal_places=4,
        null=True,
        blank=True,
    )
    day_kilowatt_hour_rate = models.DecimalField(
        verbose_name="Day Kilowatt Hour Rate",
        max_digits=8,
        decimal_places=4,
        null=True,
        blank=True,
    )
    night_rate = models.DecimalField(
        verbose_name="Night Rate", max_digits=8, decimal_places=8, null=True, blank=True
    )
    annualised_budget = models.DecimalField(
        verbose_name="Annualised Budget",
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
    commission_per_annum = models.DecimalField(
        verbose_name="Commission Per Annum",
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
    commission_per_unit = models.DecimalField(
        verbose_name="Commission Per Unit",
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
    commission_per_contract = models.DecimalField(
        verbose_name="Commission Per Contract",
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
    partner_commission = models.DecimalField(
        verbose_name="Partner Commission",
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
    smart_meter = models.CharField(
        verbose_name="Smart Meter", max_length=25, null=True, blank=True
    )
    notes = models.TextField(null=True, blank=True)
    kva = models.CharField(verbose_name="KVA", max_length=25, null=True, blank=True)
    future_contract_start_date = models.DateField(
        verbose_name="Future Contract Start Date", null=True, blank=True
    )
    future_unit_rate_1 = models.DecimalField(
        verbose_name="Future Unit Rate 1",
        max_digits=8,
        decimal_places=4,
        null=True,
        blank=True,
    )
    future_unit_rate_2 = models.DecimalField(
        verbose_name="Future Unit Rate 2",
        max_digits=8,
        decimal_places=4,
        null=True,
        blank=True,
    )
    future_unit_rate_3 = models.DecimalField(
        verbose_name="Future Unit Rate 3",
        max_digits=8,
        decimal_places=4,
        null=True,
        blank=True,
    )
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
    def days_till(self):
        today = date.today()
        days_till = self.contract_end_date - today
        days_till_stripped = str(days_till).split(",", 1)[0]
        return days_till_stripped
