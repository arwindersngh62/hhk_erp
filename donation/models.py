from django.db import models
# Create your models here.
mode_choces = [
    ('CASH', 'Cash'),
    ('INET', 'Internet Banking'),
    ('UPI', 'UPI'),
    ('IMPS', 'IMPS'),
    ('NEFT', 'NEFT'),
    ('CHEQUE', 'Cheque'),
]
#verified donation model each model is mapped to a unique member
class verified_donation(models.Model):
    rec_no = models.AutoField(primary_key=True)
    # rec_no + prefix = reiciept number
    recipt_num = models.IntegerField(default = 0)
    # member is allowed to be null in case we have an anonymous doner
    member = models.ForeignKey('supporters.supporter', on_delete=models.CASCADE,null=True)
    # optional anon_name of anonymous donor
    anon_name = models.CharField(max_length = 100,null = True,blank =True)
    amount = models.CharField(max_length = 20, blank=False)
    date_donation = models.DateField(blank=True)
    mode_donation = models.CharField(max_length = 100,default = 'CASH',choices = mode_choces)
    date_rec = models.DateField()
    # tells if it was peviously anonymous and now attached to a particular member
    migrated = models.BooleanField(default = False)
    # tells if the model is anonymous
    anon = models.BooleanField(default = False)
    # tells if the mail was successfully sent
    mail_sent = models.BooleanField(default = False)


class misc(models.Model):
    rec_no_prefix = models.IntegerField(default = 0)