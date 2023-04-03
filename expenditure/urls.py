from django.urls import path
from . import views

app_name = 'expenditure'
urlpatterns=[
    path('addexp/',views.add_exp_view,name = 'add_exp'),
    path('addadv/',views.add_adv,name = 'add_adv'),
    path('expgen/',views.generate_exp,name = 'gen_exp'),
    path('clearexp/',views.clear_exp,name = 'clearexp'),
    path('approvexp/',views.approve_exp,name = 'approvexp'),
    path('myexp/',views.my_exp,name = 'myexp'),
    path('viewexp/',views.view_exp,name = 'viewexp')
]