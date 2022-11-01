from django.core.management.base import BaseCommand, CommandError
from leases import logic


class Command(BaseCommand):
    help = "Get first five leases by ascending current rent"

    def handle(self, *args, **options):
        leases = logic.get_leases(order_by="-current_rent")
        print(leases)
