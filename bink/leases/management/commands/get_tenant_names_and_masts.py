from django.core.management.base import BaseCommand, CommandError

from leases import logic


class Command(BaseCommand):
    help = "Get tenant names and masts in dictionary form"

    def handle(self, *args, **options):
        names_and_mast_counts = logic.get_tenant_names_and_mast_counts()
        print(names_and_mast_counts)

