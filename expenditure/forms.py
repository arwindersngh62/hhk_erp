from django.forms import ModelForm,Textarea,DecimalField
from .models import expenditure,exp_items,advanced


class add_exp(ModelForm):
    class Meta:
        model = expenditure
        fields = ['event_name','event_desc','event_date','bill_amount','bill_no','bill_date','vendor_name','file']
        widgets = {
            'event_desc': Textarea(attrs={'cols':80,'rows':20}),
        }


class add_adv_form(ModelForm):
    class Meta:
        model = advanced
        fields = ['event_name','adv_desc','event_date','amount']
        widgets = {
            'adv_desc': Textarea(attrs={'cols':80,'rows':20}),
        }


