
from django.contrib import admin
from django.urls import path



from .views import student_list,district_info,district_filter,upazila_info,shop_info,create,edit_post





urlpatterns=[

     path('std/', student_list),
     path('dis/', district_info),
     path('upa/', upazila_info),
     path('shop/', shop_info, name='shop_info'),
     path('filt/<name>', district_filter),
     path('edit/<post_id>', edit_post, name='edit'),
     path('create/', create),


]
