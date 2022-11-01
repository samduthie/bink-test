from django.test import TestCase

from leases import logic, models


class LeaseTests(TestCase):
    def setup(self):
        pass  # assume fixtures have been set up to mirror migrations

    def test_get_leases_is_correct_amount(self):
        expected_amount_of_leases = 2
        leases = logic.get_leases(amount=expected_amount_of_leases)

        self.assertEqual(len(leases), expected_amount_of_leases)

    def test_get_leases_ordered_correctly(self):
        leases = logic.get_leases(order_by="-id")
        final_lease = models.Lease.objects.all().last()

        self.assertEqual(leases[0], final_lease)

    def test_get_leases_and_total_value_value_is_correct(self):
        leases, total_lease_value = logic.get_leases_and_total_value()
        expected_total_value = 0

        for lease in leases:
            expected_total_value = expected_total_value + lease.current_rent

        self.assertEqual(expected_total_value, total_lease_value["current_rent__sum"])

    def test_get_leases_between_dates(self):
        date1 = (2006, 6, 1)
        date2 = (2007, 8, 31)

        leases = logic.get_leases_between_dates(date1, date2)

        self.assertEqual(len(leases), 2)

    def test_get_tenant_names_and_mast_counts(self):
        names_and_mast_counts = logic.get_tenant_names_and_mast_counts()

        self.assertEqual(names_and_mast_counts.get("Arqiva Ltd"), 1)
