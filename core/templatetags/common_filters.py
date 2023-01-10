from datetime import date

from django import template
from django.contrib.auth.models import Group
from django.db.models import Count, Q, Sum

from account_managers.models import AccountManager
from contracts.models import Contract
from objections.models import Objection

register = template.Library()


# Statistics for contracts dashboard
# Utility Contract Numbers
@register.simple_tag
def total_contracts():
    return Contract.objects.count()


@register.simple_tag
def total_gas_contracts():
    return Contract.objects.filter(Q(utility__utility__icontains="Gas")).count()


@register.simple_tag
def total_electricity_contracts():
    return Contract.objects.filter(Q(utility__utility__icontains="Electricity")).count()


# Main Supplier Contract Count
@register.simple_tag
def total_sse_contracts():
    return Contract.objects.filter(Q(supplier__supplier__icontains="SSE")).count()


@register.simple_tag
def total_crown_contracts():
    return Contract.objects.filter(Q(supplier__supplier__icontains="Crown")).count()


@register.simple_tag
def total_corona_contracts():
    return Contract.objects.filter(Q(supplier__supplier__icontains="Corona")).count()


@register.simple_tag
def total_pozitive_contracts():
    return Contract.objects.filter(Q(supplier__supplier__icontains="Pozitive")).count()


# Main Client Contract Count
@register.simple_tag
def total_encore_contracts():
    return Contract.objects.filter(Q(client__client__icontains="Encore")).count()


@register.simple_tag
def total_hml_contracts():
    return Contract.objects.filter(Q(client__client__icontains="HML")).count()


@register.simple_tag
def total_ooc_contracts():
    return Contract.objects.filter(is_ooc=True).count()


@register.simple_tag
def total_directors_approval_contracts():
    return Contract.objects.filter(is_directors_approval=True).count()


@register.simple_tag
def total_under_objection_outstanding_contracts():
    return Objection.objects.filter(objection_status="OUTSTANDING").count()


@register.simple_tag
def total_under_objection_pending_contracts():
    return Objection.objects.filter(objection_status="PENDING").count()


# Estimated Annual Consumption


@register.simple_tag
def total_eac_electricity():
    total = Contract.objects.filter(utility__utility="Electricity").aggregate(
        TOTAL=Sum("eac")
    )["TOTAL"]
    return total


@register.simple_tag
def total_eac_gas():
    total = Contract.objects.filter(utility__utility="Gas").aggregate(TOTAL=Sum("eac"))[
        "TOTAL"
    ]
    return total


@register.simple_tag
def total_eac_under_objection_outstanding_contracts():
    total = Objection.objects.filter(objection_status="OUTSTANDING").aggregate(
        TOTAL=Sum("eac")
    )["TOTAL"]
    return total


@register.simple_tag
def total_eac_under_objection_pending_contracts():
    total = Objection.objects.filter(objection_status="PENDING").aggregate(
        TOTAL=Sum("eac")
    )["TOTAL"]
    return total


@register.simple_tag
def total_seamless_contracts():
    return Contract.objects.filter(seamless=True).count()


@register.simple_tag
def total_non_seamless_contracts():
    return Contract.objects.filter(non_seamless=True).count()


@register.simple_tag
def total_contract_value():
    total = Contract.objects.aggregate(TOTAL=Sum("contract_value"))["TOTAL"]
    return total


@register.simple_tag
def total_contract_eac_value():
    total = Contract.objects.filter(utility__utility="Electricity").aggregate(
        TOTAL=Sum("eac")
    )["TOTAL"]
    return total


@register.simple_tag
def total_sse_contract_value():
    total = Contract.objects.filter(supplier__supplier="SSE").aggregate(
        TOTAL=Sum("contract_value")
    )["TOTAL"]
    return total


@register.simple_tag
def total_electricity_contract_values():
    total = (
        Contract.objects.all()
        .filter(utility__utility="Electricity")
        .aggregate(TOTAL=Sum("contract_value"))["TOTAL"]
    )
    return total


@register.simple_tag
def total_gas_contract_values():
    total = (
        Contract.objects.all()
        .filter(utility__utility="Gas")
        .aggregate(TOTAL=Sum("contract_value"))["TOTAL"]
    )
    return total


@register.simple_tag
def total_encore_contract_values():
    total = (
        Contract.objects.all()
        .filter(client__client="Encore")
        .aggregate(TOTAL=Sum("contract_value"))["TOTAL"]
    )
    return total


@register.simple_tag
def total_hml_contract_values():
    total = (
        Contract.objects.all()
        .filter(client__client__icontains="HML")
        .aggregate(TOTAL=Sum("contract_value"))["TOTAL"]
    )
    return total


@register.simple_tag
def total_2023_contracts():
    return Contract.objects.filter(
        contract_end_date__gte="2023-01-01", contract_end_date__lte="2023-12-31"
    ).count()


@register.simple_tag
def total_2024_contracts():
    return Contract.objects.filter(
        contract_end_date__gte="2024-01-01", contract_end_date__lte="2024-12-31"
    ).count()


@register.simple_tag
def total_2025_contracts():
    return Contract.objects.filter(
        contract_end_date__gte="2025-01-01", contract_end_date__lte="2025-12-31"
    ).count()


@register.simple_tag
def total_2026_contracts():
    return Contract.objects.filter(
        contract_end_date__gte="2026-01-01", contract_end_date__lte="2026-12-31"
    ).count()


@register.simple_tag
def total_2027_contracts():
    return Contract.objects.filter(
        contract_end_date__gte="2027-01-01", contract_end_date__lte="2027-12-31"
    ).count()


# Filter based on group members
@register.filter(name="has_group")
def has_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return True if group in user.groups.all() else False


# Account Manager Total Clients
@register.simple_tag
def andrew_contracts():
    return (
        AccountManager.objects.get(
            account_manager__email="andrew@energyportfolio.co.uk"
        )
        .account_manager_clients.all()
        .count()
    )


@register.simple_tag
def laurence_contracts():
    return (
        AccountManager.objects.get(
            account_manager__email="laurence@energyportfolio.co.uk"
        )
        .account_manager_clients.all()
        .count()
    )


@register.simple_tag
def gayle_contracts():
    return (
        AccountManager.objects.get(account_manager__email="gayle@energyportfolio.co.uk")
        .account_manager_clients.all()
        .count()
    )


@register.simple_tag
def martin_contracts():
    return (
        AccountManager.objects.get(
            account_manager__email="martin@energyportfolio.co.uk"
        )
        .account_manager_clients.all()
        .count()
    )


@register.simple_tag
def total_contract_sse_value():
    total = Contract.objects.filter(supplier__supplier="SSE").aggregate(
        TOTAL=Sum("contract_value")
    )["TOTAL"]
    return total


@register.simple_tag
def total_contract_crown_value():
    total = Contract.objects.filter(supplier__supplier="Crown").aggregate(
        TOTAL=Sum("contract_value")
    )["TOTAL"]
    return total


@register.simple_tag
def total_contract_corona_value():
    total = Contract.objects.filter(supplier__supplier="Corona").aggregate(
        TOTAL=Sum("contract_value")
    )["TOTAL"]
    return total


@register.simple_tag
def total_contract_pozitive_value():
    total = Contract.objects.filter(supplier__supplier="Pozitive").aggregate(
        TOTAL=Sum("contract_value")
    )["TOTAL"]
    return total
