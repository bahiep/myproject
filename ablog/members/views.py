from typing import Generic
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.views.generic import CreateView,DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Bill, Profile
from .forms import BillForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.http import HttpResponseRedirect
# Create your views here.
# class UserRegisterView(generic.CreateView):
#     form_class=SignUpForm
#     template_name='registration/register.html'
#     success_url=reverse_lazy('login')


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST, request.FILES)
        
        # profile_form = ProfileEditForm(request.POST)
        if user_form.is_valid():
        # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            date_of_birth=user_form.cleaned_data['date']
            photo = user_form.cleaned_data['photo']
            new_user.save()
            profile = Profile.objects.create(user=new_user, date_of_birth=date_of_birth,photo=photo)
        return HttpResponseRedirect('/members/login/')
        # return render(request,'registration/register_done.html',{'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
        # profile_form = ProfileEditForm()
    return render(request,'registration/register.html',{'user_form': user_form})

# @login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,data=request.POST,files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
        return HttpResponseRedirect('/members/edit/')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,'registration/edit.html',{'user_form': user_form,'profile_form': profile_form})

class BillListView(generic.ListView):
    queryset = Bill.objects.all().order_by("-publish")
    template_name = 'registration/list_bill.html'
    context_object_name = 'Bill'
    # paginate_by=2

# class AddBillView(Generic.CreateView):
#     model=Bill
#     # form_class=BillForm
#     template_name='registration/add_bill.html'
#     fields = '__all__' 
#     # fields=('title','body')

class BillDetailView(DetailView):
    model=Bill
    template_name='registration/detail_bill.html'

def AddBill(request):
    # post = get_object_or_404(Post, pk=pk)
    form = BillForm()
    if request.method =='POST':
        form = BillForm(request.POST, request.FILES, author=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/members/bill/')
    return render(request, "registration/add_bill.html", {"form":form})

# class AddBillView(CreateView):
#     model=Bill
#     # form_class=BillForm
#     template_name='registration/add_bill.html'
#     # fields = '__all__' 
#     fields=('title','body')