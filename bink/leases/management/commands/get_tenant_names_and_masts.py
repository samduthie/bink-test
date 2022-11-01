from django.core.management.base import BaseCommand, CommandError
from django.db.models import Sum

from leases import models


class Command(BaseCommand):
    help = "Get tenant names and masts in dictionary form"

    def handle(self, *args, **options):
        tenant_names_and_mast_counts = {}

        for tenant in models.Tenant.objects.all():
            tenant_names_and_mast_counts.update(
                {tenant.tenant_name: len(models.Lease.objects.filter(tenant=tenant))}
            )

        print(tenant_names_and_mast_counts)
