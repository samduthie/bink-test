from django.db import models


class Lease(models.Model):
    property_name = models.CharField(max_length=255)
    property_address_1 = models.CharField(max_length=255)
    property_address_2 = models.CharField(max_length=255)
    property_address_3 = models.CharField(max_length=255)
    property_address_4 = models.CharField(max_length=255)
    unit_name = models.CharField(max_length=60)
    tenant_name = models.CharField(max_length=60)
    lease_start_date = models.DateField()
    lease_end_date = models.DateField()
    lease_years = models.IntegerField()
    current_rent = models.IntegerField()

