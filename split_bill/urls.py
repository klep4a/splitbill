from django.urls import path

from . import views

app_name = 'split_bill'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:bill_id>/', views.bill_detail, name='bill_detail'),
    path('<int:bill_id>/persons/', views.persons_list, name='persons_list'),
    path('<int:person_id>/detail/', views.person_detail, name='person_detail'),
]
