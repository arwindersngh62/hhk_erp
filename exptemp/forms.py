from django.forms import ModelForm,Textarea,DecimalField
from .models import expense



class add_exp(ModelForm):
    class Meta:
        model = expense
        #fields = ['added_by','event_name','expense_date','amount','is_advance','vendor_name','file','remarks']
        exclude = ['reimb_id','is_settled','added_on','expense_date','expense_head','exp','category','sub_category']
        widgets = {
            'remarks': Textarea(attrs={'cols':80,'rows':20}),
        }
        