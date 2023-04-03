from django.db import models
from django.utils import timezone


class supporter(models.Model):
    name = models.CharField(max_length=100,blank=False)
    age = models.CharField(max_length=100,null=True,blank=True)
    gender = models.CharField(max_length=15, null=True, blank=True)
    phone_no = models.CharField(max_length=20,unique=True, blank=False)
    alt_phone_no = models.CharField(max_length=20, null=True, blank=True)
    email_id = models.EmailField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    Reference = models.CharField(max_length=100, null=True, blank=True)
    pan_card = models.CharField(max_length=100, null=True, blank=True)
    address_a = models.CharField(max_length=100, null=True, blank=True)
    address_b = models.CharField(max_length=100, null=True)
    address_c = models.CharField(max_length=100, null=True)
    is_constant = models.BooleanField(default=False)
    amount = models.PositiveIntegerField(default=0,null=True, blank=True)
    is_sponsor = models.BooleanField(default=False)
    sponsee = models.CharField(max_length=300, null=True, blank=True)
    is_one_time = models.BooleanField(default=False)
    resources = models.BooleanField(default=False)
    is_si = models.BooleanField(default = False)
    si_date = models.IntegerField(null = True, blank=True)
    dob = models.DateField(null = True,blank=True)
    profession = models.CharField(max_length= 200, null = True, blank=True)
    is_verified = models.BooleanField(default=False)
    last_generated = models.IntegerField(default=0, blank=True)
    date_added = models.DateTimeField(default=timezone.now, blank=True)
    date_edited = models.DateTimeField(default=timezone.now, blank=True)

    def update_added(self):
        self.last_generated = int(timezone.localdate().month)

    def __str__(self):
        return str([self.name,self.phone_no])
