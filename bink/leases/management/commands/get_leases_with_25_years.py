from django.core.management.base import BaseCommand, CommandError

from leases import logic


class Command(BaseCommand):
    help = "Get list of 25 year leases and sum of total value"

    def handle(self, *args, **options):
        leases, total_lease_value = logic.get_leases_and_total_value()
        print(leases)
        print("total rent: ", total_lease_value)
