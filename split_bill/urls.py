from django.urls import path, include

from . import views

app_name = 'split_bill'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:bill_id>/', views.bill_detail, name='bill_detail'),
    path('<int:bill_id>/persons/', views.persons_list, name='persons_list'),
    path('<int:person_id>/detail/', views.person_detail, name='person_detail'),
    path('<int:bill_id>/final/', views.final, name='final'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('user_bills/', views.UserBillsListView.as_view(), name='user_bills'),
    # path('user_details/', views.UserBillDetailView.as_view(), name='user_details'),
]
