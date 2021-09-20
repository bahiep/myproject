from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.conf import settings
from taggit.managers import TaggableManager
from mptt.models import MPTTModel, TreeForeignKey

class Post(models.Model):
    STATUS_CHOICES = (('draft', 'Draft'),('published', 'Published'),)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique_for_date='publish')
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    body = RichTextField(blank=True, null=True)
    image=models.ImageField(null=True, blank=True, upload_to="images/")
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    tags = TaggableManager(blank=True,related_name='tag_slug')
    view_count = models.PositiveIntegerField(default=0)
    likes = models.ManyToManyField(
        User, related_name='like', default=None, blank=True)
    like_count = models.BigIntegerField(default='0')
    thumbsup = models.IntegerField(default='0')
    thumbsdown = models.IntegerField(default='0')
    thumbs = models.ManyToManyField(User, related_name='thumbs', default=None, blank=True)
    class Meta:
        ordering = ('-publish',)
    def __str__(self):
        return self.title

class Comment(MPTTModel):
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    class MPTTMeta:
        # comments on one level will be ordered by date of creation
        order_insertion_by=['post']
    # class Meta:
    #     ordering = ('-date',)
    
class Vote(models.Model):
    
    post = models.ForeignKey(Post, related_name='postid',
                             on_delete=models.CASCADE, default=None, blank=True)
    user = models.ForeignKey(User, related_name='userid',
                             on_delete=models.CASCADE, default=None, blank=True)
    vote = models.BooleanField(default=True)

