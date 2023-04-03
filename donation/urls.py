from django.urls import path,include
from . import views

app_name = 'donation'

urlpatterns = [
# opens three options of adding donations ind bulk or anon
    path('add_don/',views.add_don,name='add_don'),
    path('don_ind/',views.don_ind,name='don_ind'),
    path('don_bulk/',views.don_bulk,name='don_bulk'),
    path('don_anon/',views.don_anon,name='don_anon'),
    path('don_added/',views.don_added,name='don_added'),
    path('view_don/',views.DonationListView.as_view(),name = 'view_don'),
    path('download/',views.download_rec,name = 'download_rec'),
    path('edit_misc/',views.set_prefix,name = 'edit_misc'),
    path('export_donation/',views.export_donation,name = 'export_donations'),
    path('resend_mails/',views.resend_mails,name = 'resend_mail'),
    path('edit_don/',views.edit_don,name = 'edit_don'),
    path('don_edited',views.don_edited,name = 'don_edited')
]