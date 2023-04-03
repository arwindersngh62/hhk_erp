from django import forms
from .models import supporter

# form for adding new supporters 
class AddSupp(forms.ModelForm):
    class Meta:
        model= supporter
        exclude = ['address_b','address_c','date_added','date_edited','dob','last_generated','is_verified']
        widgets = {
        'address_a':forms.Textarea(attrs={'rows':3,'cols':10}),
        'sponsee': forms.TextInput(attrs={'disabled':'True'}),
        'amount': forms.NumberInput(attrs={'disabled':'True'}),
        'si_date': forms.NumberInput(attrs={'disabled':'True'})
        
        }
        labels = {
            'address_a' : ('Address'),
            'sponsee' : ('Name of child'),
            'is_si': ('Is SI'),
            'si_date': ('SI Date')
        }

# form for import file upload
class Uploadfiles(forms.Form):
    file = forms.FileField()

############################################################################
#                 Chunk of code which is future or past                    #
############################################################################
#earlier code for changing form kept here for backward compatability test
#####################
# class AddSupp(forms.Form):
    # name = forms.CharField(label='Name',max_length=100,required=False)
    # age = forms.IntegerField(label='Age',required = False)
    # gender = forms.CharField(label='Gender',max_length=15,required = False)
    # phone_no = forms.CharField(label='Phone Number',max_length=20)
    # alt_phone_no = forms.CharField(label='Alternative Phone No',max_length=20,required=False)
    # email_id = forms.EmailField(label='Email_Id',required=False)
    # city = forms.CharField(label='City',max_length=100,required=False)
    # Reference = forms.CharField(label='Reference',max_length=100,required=False)
    # pan_card = forms.CharField(label='Pan Card No.',max_length=100,required=False)
    # address_a = forms.CharField(label='Address',max_length=100,required=False,widget=forms.Textarea)
    # #address_b = forms.CharField(label='Address',max_length=100,required=False)
    # #address_c = forms.CharField(label='Address',max_length=100,required=False)
    # is_constant = forms.BooleanField(label='Constant',required=False)
    # amount = forms.IntegerField(label='Amount(if Contant)',required=False,disabled=True)
    # is_sponsor = forms.BooleanField(label='Child Sponsor',required=False)
    # sponsee = forms.CharField(label='Name of Child(If sponsor)',max_length=300,required=False,disabled=True)
    # is_one_time = forms.BooleanField(label='One Time',required=False)
    # resources = forms.BooleanField(label='Resources',required=False)
    # is_si = forms.BooleanField(label='SI',required=False)
    # si_date = forms.IntegerField(label='SI Date',required=False,disabled=True)
    # #dob = forms.DateField(label='Date Of Birth',required=False)
    # profession = forms.CharField(label='Profession',max_length= 200,required=False)
    
    
# later part for user to select field mappings manually.
#############################
# default_choices = [
    # ('0','one'),
    # ('1','two'),
    # ('2','three')
# ]
# class Mappingfields(forms.Form):
    # is_file = forms.BooleanField(widget=forms.HiddenInput(), initial=False,required=False)
    # name = forms.ChoiceField(label="Name",required=False,choices=default_choices)
    # age = forms.ChoiceField(label="Age",required=False,choices=default_choices)
    # gender = forms.ChoiceField(label="Gender",required=False,choices=default_choices)
    # phone_no = forms.ChoiceField(label="Phone Number",required=True,choices=default_choices)
    # alt_phone_no = forms.ChoiceField(label="Alternate Phone Number",required=False,choices=default_choices)
    # email_id = forms.ChoiceField(label="Email",required=False,choices=default_choices)
    # city = forms.ChoiceField(label="City",required=False,choices=default_choices)
    # Reference = forms.ChoiceField(label="Reference",required=False,choices=default_choices)
    # pan_card = forms.ChoiceField(label="Pan Card",required=False,choices=default_choices)
    # address_a = forms.ChoiceField(label="Address",required=False,choices=default_choices)
    # is_constant = forms.ChoiceField(label="Constant",required=False,choices=default_choices)
    # amount = forms.ChoiceField(label="Amount",required=False,choices=default_choices)
    # is_sponsor = forms.ChoiceField(label="Sponsor",required=False,choices=default_choices)
    # sponsee = forms.ChoiceField(label="Sponsee",required=False,choices=default_choices)
    # is_one_time = forms.ChoiceField(label="ONe TIme",required=False,choices=default_choices)
    # resources = forms.ChoiceField(label="Resources",required=False,choices=default_choices)
    # is_si = forms.ChoiceField(label="SI",required=False,choices=default_choices)
    # si_date = forms.ChoiceField(label="SI Date",required=False,choices=default_choices)
    # dob = forms.ChoiceField(label="DOP",required=False,choices=default_choices)
    # profession = forms.ChoiceField(label="Profession",required=False,choices=default_choices)