from django.urls import path

from . import views

app_name = 'split_bill'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:bill_id/>', views.bill_details, name='bill_details'),

]
