from datetime import date

from django.core.management.base import BaseCommand, CommandError

from leases import logic


class Command(BaseCommand):
    help = (
        "Get rentals with lease start date between 1st June 1999 and 31st August 2007"
    )

    def handle(self, *args, **options):
        date1 = (1999, 6, 1)
        date2 = (2007, 8, 31)

        leases = logic.get_leases_between_dates(date1, date2)

        for lease in leases:
            print(f"{lease['name']}, End Date: {lease['date']}")
