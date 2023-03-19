from django.db import models
from users.models import Staff, Customer, User

# Create your models here.
class AdministrativeRegions(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    code_name_en = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'administrative_regions'


class AdministrativeUnits(models.Model):
    id = models.IntegerField(primary_key=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    full_name_en = models.CharField(max_length=255, blank=True, null=True)
    short_name = models.CharField(max_length=255, blank=True, null=True)
    short_name_en = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    code_name_en = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'administrative_units'


class Provinces(models.Model):
    code = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    full_name = models.CharField(max_length=255)
    full_name_en = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    administrative_unit = models.ForeignKey(AdministrativeUnits, models.DO_NOTHING, blank=True, null=True)
    administrative_region = models.ForeignKey(AdministrativeRegions, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'provinces'


class Districts(models.Model):
    code = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    full_name_en = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    province_code = models.ForeignKey('Provinces', models.DO_NOTHING, db_column='province_code', blank=True, null=True)
    administrative_unit = models.ForeignKey(AdministrativeUnits, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'districts'


class Wards(models.Model):
    code = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    full_name_en = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    district_code = models.ForeignKey(Districts, models.DO_NOTHING, db_column='district_code', blank=True, null=True)
    administrative_unit = models.ForeignKey(AdministrativeUnits, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wards'
    
    def __str__(self) -> str:
        return self.full_name


class AddressUser(models.Model):
    specific = models.CharField(max_length=255)
    ward = models.ForeignKey(Wards, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="address_user_user")

    def __str__(self) -> str:
        return f'{self.specific}, {self.ward.full_name} {self.ward.district_code.full_name}, {self.ward.district_code.province_code.full_name}'


class DeliveryAddress(models.Model):
    specific = models.CharField(max_length=255)
    ward = models.ForeignKey(Wards, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    is_default = models.BooleanField(default=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="delivery_address_customer")
    recipient_first_name = models.CharField(max_length=50)
    recipient_last_name = models.CharField(max_length=50)
