from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('withdraw', views.WithdrawView.as_view(), name='withdraw'),
    path('add_withdraw', views.Withdraw, name='add_withdraw'),
    path('huongdanmuasam', views.ShopingTutorial, name='huongdanmuasam'),
    path('huongdanruttien', views.WithdrawTutorial, name='huongdanruttien'),
]