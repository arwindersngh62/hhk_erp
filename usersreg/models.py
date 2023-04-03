from django.db import models
from django.contrib.auth.models import User

# Create your models here.
choices_type = [
    ('vol','Volunter'),
    ('finmem','Finance_Member'),
    ('fihead','Finance_Head'),
    ('dir','Director'),
    ('pres','President')]


class member(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    type = models.CharField(max_length=50,choices = choices_type)