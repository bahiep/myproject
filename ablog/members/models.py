from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d',blank=True)
    cash = models.IntegerField(default=0)
    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

class Bill(models.Model):
    # STATUS_CHOICES = (('draft', 'Draft'),('published', 'Published'),)
    title = models.CharField(max_length=250)
    # slug = models.SlugField(max_length=250,unique_for_date='publish')
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='bill_author')
    body = RichTextField(blank=True, null=True)
    image=models.ImageField(null=True, blank=True, upload_to='users/%Y/%m/%d')
    publish = models.DateTimeField(auto_now_add=True)
    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)
    # status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    def get_absolute_url(self):
        return reverse('list_bill')
    class Meta:
        ordering = ('-publish',)
    def __str__(self):
        return self.title
    

