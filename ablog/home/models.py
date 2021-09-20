from django.db import models
from django.contrib.auth.models import User
from django.db.models.aggregates import Max
from members.models import Profile

# Create your models here.
class Shop(models.Model):
    # STATUS_CHOICES = (('draft', 'Draft'),('published', 'Published'),)
    title = models.CharField(max_length=250)
    # slug = models.SlugField(max_length=250,unique_for_date='publish')
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField(blank=True, null=True)
    image=models.ImageField(null=True, blank=True, upload_to="home/")
    publish = models.DateTimeField(auto_now_add=True)
    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)
    # status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    class Meta:
        ordering = ('-publish',)
    def __str__(self):
        return self.title

class Withdraw(models.Model):
    # STATUS_CHOICES = (('draft', 'Draft'),('published', 'Published'),)
    fullname = models.CharField(max_length=250)
    # slug = models.SlugField(max_length=250,unique_for_date='publish')
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    bankname = models.CharField(max_length=250)
    accountnumber=models.CharField(max_length=250)
    cashwithdraw=models.IntegerField(default=0)
    status = models.CharField(max_length=250, default='Đang xử lý')
    publish = models.DateTimeField(auto_now_add=True)
    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)
    # status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    # def get_absolute_url(self):
    #     return reverse('list_bill')
    class Meta:
        ordering = ('-publish',)
    def __str__(self):
        return self.fullname