from django.core.management.base import BaseCommand, CommandError
from leases import models


class Command(BaseCommand):
    help = "Get first five leases by ascending current rent"

    def handle(self, *args, **options):
        leases = models.Lease.objects.all().order_by("-current_rent")
        print(leases[:5])
