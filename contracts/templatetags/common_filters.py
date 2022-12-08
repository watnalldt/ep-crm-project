from datetime import date

from django import template
from django.db.models import Count, Q, Sum

from contracts.models import Contract

register = template.Library()


@register.simple_tag
def total_contracts():
    return Contract.objects.count()


@register.simple_tag
def total_gas_contracts():
    return Contract.objects.filter(Q(utility__utility__icontains="Gas")).count()


@register.simple_tag
def total_electricity_contracts():
    return Contract.objects.filter(Q(utility__utility__icontains="Electricity")).count()


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
def total_under_objection_contracts():
    return Contract.objects.filter(under_objection=True).count()


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
def total_2022_contracts():
    return Contract.objects.filter(contract_end_date__lte="2022-12-31").count()
