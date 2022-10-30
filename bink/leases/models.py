from django.db import models


class Tenant(models.Model):
    def __repr__(self):
        return f'{self.tenant_name}'

    tenant_name = models.CharField(max_length=60)


class Property(models.Model):
    def __repr__(self):
        return f'{self.property_name}'

    property_name = models.CharField(max_length=255)
    property_address_1 = models.CharField(max_length=255)
    property_address_2 = models.CharField(max_length=255)
    property_address_3 = models.CharField(max_length=255)
    property_address_4 = models.CharField(max_length=255)
    unit_name = models.CharField(max_length=60)


class Lease(models.Model):
    def __repr__(self):
        return f'{self.id}, {self.property}'

    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.CASCADE,
    )

    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
    )

    lease_start_date = models.DateField()
    lease_end_date = models.DateField()
    lease_years = models.IntegerField()
    current_rent = models.FloatField()
