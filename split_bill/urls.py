from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('<int:bill.id/>', views.DetailView.as_view(), name='detail'),
]
