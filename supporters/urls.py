from django.urls import path
from . import views

app_name = 'supporters'
urlpatterns = [
    path('add_supp/',views.add_supp,name = 'add_supp'),
    path('edit_supp/',views.supp_edited,name = 'supp_edited'),
    path('supp_edited/',views.edit_supp,name = 'edit_supp'),
    path('view_supp/',views.view_supp,name = 'view_supp'),
    path('del_supp/',views.del_supp,name = 'del_supp'),
    path('deleted/',views.delete, name='deleted'),
    path('view_don/',views.view_don,name = 'view_don'),
    path('import/',views.import_supp,name = 'import'),
    path('don_details/',views.view_don,name = 'don_details'),
    path('export/',views.export_supporters,name = 'export_supporters')
    ]