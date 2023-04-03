from django.forms import ModelForm,CharField,DateField,Form,FileField
from .models import verified_donation,misc

# donations which have been verified are cptured using this form directly fetches specified model fields of verified_donation model
class IndonForm(ModelForm):
    class Meta:
        model = verified_donation
        fields = ['amount','mode_donation']

# donations which have are anonymous are cptured using this form directly fetches specified fields of verified_donation model

class AnondonForm(ModelForm):
    amount = CharField(required=True)
    class Meta:
        model = verified_donation
        fields = ['anon_name','amount','mode_donation']

# sets up misc values , this is needed to ensure that the prefix to be added to the reciept number can be changed as needed

class miscForm(ModelForm):
    class Meta:
        model = misc
        fields = ['rec_no_prefix']
    

# form to handle uploaded files

class Uploadfiles(Form):
    file = FileField()