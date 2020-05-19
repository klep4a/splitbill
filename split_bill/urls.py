from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views

app_name = 'split_bill'


class MyHackedView(auth_views.PasswordResetView):
    success_url = reverse_lazy('split_bill:password_reset_done')


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:bill_id>/', views.bill_detail, name='bill_detail'),
    path('<int:bill_id>/persons/', views.persons_list, name='persons_list'),
    path('<int:person_id>/detail/', views.person_detail, name='person_detail'),
    path('<int:bill_id>/final/', views.final, name='final'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('user_bills/', views.UserBillsListView.as_view(), name='user_bills'),
    path('register/', views.register, name='register'),
    path('profile/', views.view_profile, name='profile'),
    path('password_reset/', MyHackedView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('split_bill:password_reset_complete')),
         name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
]
