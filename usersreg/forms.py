from django import forms

choices_type = [
    ('vol','Volunter'),
    ('finmem','Finance_Member'),
    ('fihead','Finance_Head'),
    ('dir','Director'),
    ('pres','President')]


class memberCreate(forms.Form):
    u_name = forms.CharField(label ='Username',max_length=70)
    password = forms.CharField(label='Password',max_length=80)
    email = forms.CharField(label = 'Email Id',max_length=100)
    f_name = forms.CharField(label='First Name',max_length=100)
    l_name = forms.CharField(label='Last Name',max_length=100)
    type = forms.ChoiceField(label = 'Type',choices=choices_type)
