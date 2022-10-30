from datetime import date

from django.core.management.base import BaseCommand, CommandError
from django.db.models import Sum

from leases import models


class Command(BaseCommand):
    help = 'Get rentals with lease start date between 1st June 1999 and 31st August 2007'

    def handle(self, *args, **options):
        leases = models.Lease.objects.filter(
            lease_start_date__gte=date(1999, 6, 1),
            lease_start_date__lte=date(2007, 8, 31),
        )

        for lease in leases:
            formatted_date = lease.lease_start_date.strftime('%d/%m/%Y')
            print(f'{lease.property.property_name}, End Date: {formatted_date}')
