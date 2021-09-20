from django.urls import path
from .views import BillDetailView, AddBill, register, edit, BillListView

urlpatterns = [
    path('register/',register,name='register'),
    path('edit/', edit, name='edit'),
    # path('add_bill/', AddBillView.as_view(), name='add_bill'),
    path('add_bill/', AddBill, name='add_bill'),
    path('bill/', BillListView.as_view(), name='list_bill'),
    path('detail/<int:pk>', BillDetailView.as_view(), name='detail_bill'),
]