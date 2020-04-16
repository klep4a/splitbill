from django.urls import path

from . import views

app_name = 'split_bill'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:bill_id>/', views.bill_detail, name='bill_detail'),
    path('<int:bill_id>/person/', views.PersonsListView.as_view(), name='persons_list'),
    path('<int:bill_id>/', views.PersonDetailView.as_view(), name='person_detail'),
]
