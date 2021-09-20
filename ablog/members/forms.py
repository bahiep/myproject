from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import models
from django.db.models.fields import CharField, DateField
from django.db.models.fields.files import ImageField
from .models import Bill, Profile

class LoginForm(forms.ModelForm):
    username=forms.CharField(label="Tài khoản")
    password=forms.CharField(label="Mật khẩu")

class UserEditForm(forms.ModelForm):
    last_name = forms.CharField(label="Họ")
    first_name = forms.CharField(label="Tên")
    email = forms.EmailField(label="E-mail")
    class Meta:
        model = User
        fields = ( 'last_name','first_name', 'email')
class ProfileEditForm(forms.ModelForm):
    date_of_birth=forms.DateField(label="Ngày sinh")
    photo=forms.ImageField(label="Ảnh đại diện")
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')

# class SignUpForm(UserCreationForm):
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
#     first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
#     last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))

#     class Meta:
#         model = User
#         fields = ('username', 'first_name','last_name','email','password1','password2')

#     def __init__(self,*args,**kwargs):
#         super(SignUpForm, self).__init__(*args, **kwargs)

#         self.fields['username'].widget.attrs['class'] = 'form-control'
#         self.fields['password1'].widget.attrs['class'] = 'form-control'
#         self.fields['password2'].widget.attrs['class'] = 'form-control'

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Tài khoản')
    last_name = forms.CharField(label='Họ')
    first_name = forms.CharField(label='Tên')
    email = forms.EmailField(label='E-mail')
    password = forms.CharField(label='Mật khẩu',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Nhập lại mật khẩu',widget=forms.PasswordInput)
    date = forms.DateField()
    # photo = Profile.photo
    photo =forms.ImageField(label='Ảnh đại diện')
    
    class Meta:
        model = User
        fields = ('username','last_name', 'first_name', 'email','photo')
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

# class BillForm(forms.ModelForm):
#     class Meta:
#         model = Bill
#         fields = ('title','author','body','image')
#         # widgets={
#         #     'title':forms.TextInput(attrs={'class':'form-control','placeholder':'This is title'}),
#         #     # 'title_tag':forms.TextInput(attrs={'class':'form-control'}),
#         #     'author':forms.Select(attrs={'class':'form-control'}),
#         #     # 'category':forms.Select(choices=choice_list,attrs={'class':'form-control'}),
#         #     'body':forms.Textarea(attrs={'class':'form-control'}),

#         # }

class BillForm(forms.ModelForm):
    title=forms.CharField(label="Tiêu đề")
    body=forms.CharField(label="Nội dung")
    image=forms.ImageField(label="Hình xác nhận mua hàng")
    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author', None)
        # self.post = kwargs.pop('post', None)
        form = super().__init__(*args, **kwargs)
        
    def save(self, commit=True):
        bill=super().save(commit=False)
        bill.author=self.author
        # comment.post = self.post
        bill.save()
    class Meta:
        model = Bill
        fields = ["title","body","image"] 
        widgets={          
            'body':forms.Textarea(attrs={'class':'form-control form-control-sm', 'rows':'3'}),
        }