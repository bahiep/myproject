from home.models import Shop, Withdraw
from .forms import WithdrawForm
from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponseRedirect
# Create your views here.
class HomeListView(ListView):
    queryset = Shop.objects.all().order_by("publish")
    template_name = 'home.html'
    context_object_name = 'Shop'
    # paginate_by=2

class WithdrawView(ListView):
    queryset = Withdraw.objects.all().order_by("-publish")
    template_name = 'withdraw.html'
    context_object_name = 'Withdraw'
    # paginate_by=2

def Withdraw(request):
    # post = get_object_or_404(Post, pk=pk)
    form = WithdrawForm()
    if request.method =='POST':
        form = WithdrawForm(request.POST, author=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/withdraw')
    return render(request, "add_withdraw.html", {"form":form})

def ShopingTutorial(request):
    # return HttpResponseRedirect('/huongdanmuasam')
    return render(request, "huongdanmuasam.html", {})

def WithdrawTutorial(request):
    return render(request, "huongdanruttien.html", {})