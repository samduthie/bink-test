from django.core.management.base import BaseCommand, CommandError
from django.db.models import Sum

from leases import models


class Command(BaseCommand):
    help = 'Get list of 25 year leases and sum of total value'

    def handle(self, *args, **options):
        leases = models.Lease.objects.filter(lease_years=25)
        total_lease_value = leases.aggregate(Sum('current_rent'))
        print(leases)
        print("total rent: ", total_lease_value)
