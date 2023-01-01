from admin_auto_filters.filters import AutocompleteFilter
from django.contrib import admin
from import_export import fields, resources
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
from rangefilter.filters import DateRangeFilter

from clients.models import Client
from utilities.models import Supplier, Utility

from .models import Contract


class ContractResource(resources.ModelResource):

    client = fields.Field(
        column_name="client",
        attribute="client",
        widget=ForeignKeyWidget(Client, "client"),
    )

    supplier = fields.Field(
        column_name="supplier",
        attribute="supplier",
        widget=ForeignKeyWidget(Supplier, "supplier"),
    )

    utility = fields.Field(
        column_name="utility",
        attribute="utility",
        widget=ForeignKeyWidget(Utility, "utility"),
    )

    class Meta:
        model = Contract
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ("id",)
        export_order = [
            "id",
            "seamless",
            "non_seamless",
            "dwellent_id",
            "bid_id",
            "property_reference",
            "portal_status",
            "client",
            "is_directors_approval",
            "business_name",
            "company_reg_number",
            "utility",
            "top_line",
            "mpan_mpr",
            "meter_serial_number",
            "building_name",
            "site_address",
            "billing_address",
            "supplier",
            "contract_start_date",
            "contract_end_date",
            "account_number",
            "eac",
            "day_consumption",
            "night_consumption",
            "vat",
            "contract_value",
            "standing_charge",
            "sc_frequency",
            "unit_rate_1",
            "unit_rate_2",
            "unit_rate_3",
            "feed_in_tariff",
            "seamless_status",
            "profile",
            "is_ooc",
            "service_type",
            "pence_per_kilowatt",
            "day_kilowatt_hour_rate",
            "night_rate",
            "annualised_budget",
            "commission_per_annum",
            "commission_per_unit",
            "commission_per_contract",
            "partner_commission",
            "smart_meter",
            "notes",
            "kva",
            "future_contract_start_date",
            "future_unit_rate_1",
            "future_unit_rate_2",
            "future_unit_rate_3",
        ]


class ClientFilter(AutocompleteFilter):
    title = "Client"  # display title
    field_name = "client"  # name of the foreign key field


class SupplierFilter(AutocompleteFilter):
    title = "Supplier"  # display title
    field_name = "supplier"  # name of the foreign key field


class UtilityTypeFilter(AutocompleteFilter):
    title = "Utility Type"  # display title
    field_name = "utility"  # name of the foreign key field

    def get_rangefilter_contract_end_date_title(self, request, field_path):
        return "Contract End Date"

    def get_rangefilter_contract_start_date_title(self, request, field_path):
        return "Contract Start Date"


class ContractAdmin(ImportExportModelAdmin):
    show_full_result_count = False
    list_select_related = ("client", "supplier", "utility")
    resource_class = ContractResource
    list_per_page = 10
    list_display = (
        "id",
        "business_name",
        "client",
        "site_address",
        "supplier",
        "utility",
        "meter_serial_number",
        "mpan_mpr",
        "eac",
        "contract_start_date",
        "contract_end_date",
        "is_ooc",
        "is_directors_approval",
    )
    fieldsets = (
        (
            "Site Information",
            {
                "description": "Enter the site details",
                "fields": (
                    ("client", "business_name"),
                    "site_address",
                    "supplier",
                    "utility",
                    "meter_serial_number",
                    "mpan_mpr",
                    "top_line",
                    "vat",
                ),
            },
        ),
        (
            "Contract Information",
            {
                "description": "Contract Information",
                "fields": (
                    (
                        "account_number",
                        "company_reg_number",
                    ),
                    "is_directors_approval",
                    "seamless",
                    "non_seamless",
                ),
            },
        ),
        (
            "Contract Date Details",
            {
                "description": "Enter the following details",
                "fields": (
                    (
                        "contract_start_date",
                        "contract_end_date",
                    ),
                    "is_ooc",
                ),
            },
        ),
        (
            "Seamless Contract Information",
            {
                "description": "The following only applies to seamless contracts",
                "classes": ("collapse",),
                "fields": (
                    (
                        "dwellent_id",
                        "bid_id",
                        "property_reference",
                        "portal_status",
                    ),
                    ("building_name", "billing_address"),
                    ("day_consumption", "night_consumption", "contract_value"),
                    ("standing_charge", "sc_frequency"),
                    ("unit_rate_1", "unit_rate_2", "unit_rate_3"),
                    "seamless_status",
                ),
            },
        ),
        (
            "Service Information",
            {
                "description": "Enter the following data",
                "fields": ("eac", "profile", "service_type", "feed_in_tariff"),
            },
        ),
        (
            "Rates",
            {
                "description": "Enter the following data",
                "fields": (
                    "pence_per_kilowatt",
                    "day_kilowatt_hour_rate",
                    "night_rate",
                    "annualised_budget",
                ),
            },
        ),
        (
            "Commissons",
            {
                "description": "Enter the following",
                # Enable a Collapsible Section
                "classes": ("collapse",),
                "fields": (
                    "commission_per_annum",
                    "commission_per_unit",
                    "partner_commission",
                ),
            },
        ),
        (
            "Future Contract Information",
            {
                "description": "Enter future contract information",
                "fields": (
                    "future_contract_start_date",
                    "future_unit_rate_1",
                    "future_unit_rate_2",
                    "future_unit_rate_3",
                ),
            },
        ),
        ("Notes", {"description": "Additional Information", "fields": ("notes",)}),
    )
    list_filter = [
        "non_seamless",
        "seamless",
        "portal_status",
        ClientFilter,
        SupplierFilter,
        UtilityTypeFilter,
        "is_ooc",
        "is_directors_approval",
        ("contract_end_date", DateRangeFilter),
        ("contract_start_date", DateRangeFilter),
        "vat",
    ]
    autocomplete_fields = [
        "client",
        "supplier",
    ]
    search_help_text = (
        "Search by MPAN/MPR or Business Name, Client Name, Meter Serial Number"
    )
    search_fields = (
        "business_name",
        "client__client",
        "mpan_mpr",
        "contract_end_date",
        "meter_serial_number",
        "site_address",
        "id",
    )
    ordering = ["id"]
    date_hierarchy = "contract_end_date"


admin.site.register(Contract, ContractAdmin)
