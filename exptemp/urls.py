from django.urls import path
from . import views

app_name = 'exptemp'
urlpatterns=[
    path('addexp/',views.add_exp_view,name = 'add_exp'),
    path('genexp/',views.success,name = 'generate_exp'),
    path('storeexp/',views.generate_exp,name = 'store_exp'),
    path('appr_success/',views.appr_success,name = 'appr_success'),
 	path('viewexp/',views.view_old,name = 'viewoldexp'),
    path('settleexp/',views.settle_exp,name = 'settleexp'),  
    path('detailexp/<int:key_id>/', views.detail_exp, name='detailexp'),
    path('settleexpform/',views.settle_exp_form,name = 'settleexpform'),
	path('settled/',views.settled_view,name = 'settled'),
]