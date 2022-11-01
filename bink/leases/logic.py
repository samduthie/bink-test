from datetime import date

from django.db.models import Sum

from leases import models


def get_leases(amount=5, order_by="id"):
    leases = models.Lease.objects.all().order_by(order_by)
    return leases[:amount]


def get_leases_and_total_value(lease_years=25):
    leases = models.Lease.objects.filter(lease_years=lease_years)
    total_lease_value = leases.aggregate(Sum("current_rent"))
    return leases, total_lease_value


def get_leases_between_dates(date1, date2):
    leases = models.Lease.objects.filter(
        lease_start_date__gte=date(*date1),
        lease_start_date__lte=date(*date2),
    )

    leases_between_date = [
        {
            "name": lease.property.property_name,
            "date": lease.lease_start_date.strftime("%d/%m/%Y"),
        }
        for lease in leases
    ]

    return leases_between_date


def get_tenant_names_and_mast_counts():
    tenant_names_and_mast_counts = {}

    for tenant in models.Tenant.objects.all():
        tenant_names_and_mast_counts.update(
            {tenant.tenant_name: len(models.Lease.objects.filter(tenant=tenant))}
        )

    return tenant_names_and_mast_counts
