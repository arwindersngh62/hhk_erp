from django.db import models
from usersreg.models import member
from django.utils import timezone


choices = [
    ('prog','Program Cost'),
    ('admin','Administrative Cost'),
    ('funds','Fundraising Cost')
]


choices_sub = []
choices_cat=[]

class advanced(models.Model):
    adv_id = models.IntegerField(primary_key=True)
    added_by = models.ForeignKey(member,on_delete=models.CASCADE)
    event_name = models.CharField(max_length=250)
    adv_desc = models.CharField(max_length=1000)
    event_date = models.DateField()
    added_on = models.DateField(default = timezone.now())
    is_cleared = models.BooleanField(default = False)
    status = models.CharField(max_length=250,default= 'Submitted')
    is_attached = models.BooleanField(default = False)
    amount = models.DecimalField(default=0,decimal_places=2,max_digits=15)
    amount_paid = models.DecimalField(default=0,decimal_places=2,max_digits=15)

class expenditure(models.Model):
    reimb_id = models.IntegerField(primary_key=True)
    added_by = models.ForeignKey(member,on_delete=models.CASCADE,default=None)
    event_name = models.CharField(max_length=250, null=True, blank=True)
    event_desc = models.CharField(max_length=250,choices=choices)
    event_date = models.DateField()
    bill_amount = models.DecimalField(default=0,decimal_places=2,max_digits=15)
    paid_amount = models.DecimalField(default=0,decimal_places=2,max_digits=20)
    bill_no = models.CharField(max_length=250)
    bill_date = models.DateField(default = timezone.now())
    vendor_name = models.CharField(max_length=250)
    is_advanced = models.BooleanField(default=False)
    adv_id = models.ForeignKey(advanced,on_delete=models.CASCADE)
    adv_amount = models.DecimalField(default=0,decimal_places=3,max_digits=8)
    is_approved = models.BooleanField(default=False)
    is_cleared = models.BooleanField(default=False)
#    amount_cleared = DecimalField(default=0,decimal_places=2,max_digits=15)

#    approved_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='approver',default=None)
#    cleared_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='clearer',default=None)
    added_on = models.DateField(default = timezone.now())
    file = models.FileField(null = True)


class exp_items(models.Model):
    exp = models.ForeignKey(expenditure,on_delete=models.CASCADE)
    desc = models.CharField(max_length=1000)
    price = models.DecimalField(decimal_places=2,max_digits=20,default = 0)
    qty = models.IntegerField(default = 1)
    amount = models.DecimalField(decimal_places=2,max_digits=20)
    


class approved(models.Model):
	exp = models.ForeignKey(expenditure,on_delete=models.CASCADE)
	approved_by = models.ForeignKey(member,on_delete=models.CASCADE,default=None)
	approval_date = models.DateField(timezone.now())
	expense_head = models.CharField(max_length=250)
	category = models.CharField(max_length=250)
	sub_category = models.CharField(max_length=250)
	amount_approved = models.DecimalField(default=0,decimal_places=2,max_digits=15)
	approve_comments = models.CharField(max_length=1000)


class cleared(models.Model):
    exp = models.ForeignKey(expenditure,on_delete=models.CASCADE)
    is_adv = models.BooleanField(default = False)
    cleared_by = models.ForeignKey(member,on_delete=models.CASCADE,default=None)
    cleared_date = models.DateField(timezone.now())
    amount_cleared = models.DecimalField(default=0,decimal_places=2,max_digits=15)
    clear_comments = models.CharField(max_length=1000)