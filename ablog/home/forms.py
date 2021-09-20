from django import forms
from .models import Withdraw

class WithdrawForm(forms.ModelForm):
    fullname=forms.CharField(label="Họ và tên")
    bankname=forms.CharField(label="Ngân hàng / Momo")
    accountnumber=forms.CharField(label="Số tài khoản / Số điện thoại")
    cashwithdraw=forms.CharField(label="Số tiền cần rút")
    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author', None)
        # self.post = kwargs.pop('post', None)
        form = super().__init__(*args, **kwargs)
        
    def save(self, commit=True):
        withdraw=super().save(commit=False)
        withdraw.author=self.author
        # comment.post = self.post
        withdraw.save()
    class Meta:
        model = Withdraw
        fields = ["fullname","bankname","accountnumber","cashwithdraw"] 
        
