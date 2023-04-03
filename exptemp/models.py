from django.db import models
from django.utils import timezone
from usersreg.models import member

# Create your models here.
class settled(models.Model):
    settled_by = models.ForeignKey(member,on_delete=models.CASCADE,default=None)
    settle_date = models.DateField(default = timezone.now())
    payment_date = models.DateField()
    amount_approved = models.DecimalField(default=0,decimal_places=2,max_digits=15)
    settled_comments = models.CharField(max_length=1000)


class expense(models.Model):
    reimb_id = models.IntegerField(primary_key=True)
    exp = models.ForeignKey(settled,on_delete=models.CASCADE,null =True)
    added_by = models.CharField(max_length=250, null=False, blank=False)
    event_name = models.CharField(max_length=250, null=True, blank=True)
    expense_date = models.DateField(null = True)
    amount = models.DecimalField(default=0,decimal_places=2,max_digits=15)
    vendor_name = models.CharField(max_length=250,null = True ,  blank = True)
    is_advance = models.BooleanField(default=False)
    is_settled = models.BooleanField(default=False)
    added_on = models.DateField(default = timezone.now())
    file = models.FileField(null = True,blank = True)
    remarks = models.CharField(max_length=1000,null = True,blank = True)
    expense_head = models.CharField(max_length=250,null = True)
    category = models.CharField(max_length=250, null = True)
    sub_category = models.CharField(max_length=250, null = True)



