from re import search
from django.db.models.expressions import Value
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.base import View
from django.views.generic.edit import FormView
from .models import Post, Comment, Vote
from .forms import CommentForm
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.db.models import Q
from taggit.models import Tag, TaggedItemBase
from django.db.models import Count

from blog import models

# Create your views here.
class PostListView(ListView):
    queryset = Post.objects.all().order_by("-publish")
    template_name = 'blog/blog.html'
    context_object_name = 'Post'
    paginate_by=2

def TagList(request,tag_slug):
    tag = Post.objects.filter(tags__slug__in=[tag_slug])
    return render(request,'blog/tag_filter.html',{'tag':tag})
       

class PostDisplay(SingleObjectMixin, View):
    model = Post
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.view_count += 1
        self.object.save()
        post = self.get_context_data(object=self.object)
        
        return render(request, 'blog/detail.html', post)

    def get_context_data(self, **kwargs):
        context = super(PostDisplay, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.get_object())
        context['form'] = CommentForm
        stuff=get_object_or_404(Post,id=self.kwargs['pk'])
        liked = False
        thumbsuped = False
        thumbsdowned = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["liked"] = liked
        stuff2 = Vote.objects.filter(post=self.get_object())
        xxx = stuff2.filter(user=self.request.user)
        if xxx.filter(vote=True).exists():
            thumbsuped = True
        if xxx.filter(vote=False).exists():
            thumbsdowned = True
        context["thumbsuped"] = thumbsuped
        context["thumbsdowned"] = thumbsdowned
        abc = Tag.objects.all()
        context["abc"] = abc
        
        return context

class PostComment(FormView):
    form_class = CommentForm
    
    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({"error": form.errors}, status=400)
        else:
            return JsonResponse({"error": "Invalid form and request"}, status=400)

    def form_valid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form.instance.author = self.request.user
            post = Post.objects.get(pk=self.kwargs['pk'])
           
            form.instance.post = post
            comment_instance = form.save()
            ser_comment = serializers.serialize("json", [comment_instance, ])
            return JsonResponse({"new_comment": ser_comment}, status=200)
        else:
            return JsonResponse({"error": "Error occured during request"}, status=400)

class PostDetail(View):
    def get(self, request, *args, **kwargs):
        view = PostDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PostComment.as_view()
        return view(request, *args, **kwargs)


def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm()
    if request.method =='POST':
        form = CommentForm(request.POST, author=request.user, post=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    return render(request, "blog/detail.html", {"post":post, "form":form})

def search_venues(request):
    if request.method == "POST":
        searched=request.POST['searched']
        venues = Post.objects.filter(title__contains=searched)
        return render(request,'blog/search-venues.html',{'searched':searched, 'venues':venues})
    else:
        return render(request,'blog/search-venues.html',{})

@ login_required
def like(request):
    if request.POST.get('action') == 'post':
        result = ''
        remove = False
        id = int(request.POST.get('postid'))
        post = get_object_or_404(Post, id=id)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            post.like_count -= 1
            result = post.like_count
            remove = True
            post.save()
        else:
            post.likes.add(request.user)
            post.like_count += 1
            result = post.like_count
            post.save()

        return JsonResponse({'result': result, 'remove':remove })

def thumbs(request):
    
    if request.POST.get('action') == 'thumbs':

        id = int(request.POST.get('postid'))
        button = request.POST.get('button')
        update = Post.objects.get(id=id)

        if update.thumbs.filter(id=request.user.id).exists():

            # Get the users current vote (True/False)
            q = Vote.objects.get(
                Q(post_id=id) & Q(user_id=request.user.id))
            evote = q.vote

            if evote == True:

                # Now we need action based upon what button pressed

                if button == 'thumbsup':

                    update.thumbsup = F('thumbsup') - 1
                    update.thumbs.remove(request.user)
                    update.save()
                    update.refresh_from_db()
                    up = update.thumbsup
                    down = update.thumbsdown
                    q.delete()

                    return JsonResponse({'up': up, 'down': down, 'remove': 'none'})

                if button == 'thumbsdown':

                    # Change vote in Post
                    update.thumbsup = F('thumbsup') - 1
                    update.thumbsdown = F('thumbsdown') + 1
                    update.save()

                    # Update Vote

                    q.vote = False
                    q.save(update_fields=['vote'])

                    # Return updated votes
                    update.refresh_from_db()
                    up = update.thumbsup
                    down = update.thumbsdown

                    return JsonResponse({'up': up, 'down': down})

            pass

            if evote == False:

                if button == 'thumbsup':

                    # Change vote in Post
                    update.thumbsup = F('thumbsup') + 1
                    update.thumbsdown = F('thumbsdown') - 1
                    update.save()

                    # Update Vote

                    q.vote = True
                    q.save(update_fields=['vote'])

                    # Return updated votes
                    update.refresh_from_db()
                    up = update.thumbsup
                    down = update.thumbsdown

                    return JsonResponse({'up': up, 'down': down})

                if button == 'thumbsdown':

                    update.thumbsdown = F('thumbsdown') - 1
                    update.thumbs.remove(request.user)
                    update.save()
                    update.refresh_from_db()
                    up = update.thumbsup
                    down = update.thumbsdown
                    q.delete()

                    return JsonResponse({'up': up, 'down': down, 'remove': 'none'})

        else:        # New selection

            if button == 'thumbsup':
                update.thumbsup = F('thumbsup') + 1
                update.thumbs.add(request.user)
                update.save()
                # Add new vote
                new = Vote(post_id=id, user_id=request.user.id, vote=True)
                new.save()
            else:
                # Add vote down
                update.thumbsdown = F('thumbsdown') + 1
                update.thumbs.add(request.user)
                update.save()
                # Add new vote
                new = Vote(post_id=id, user_id=request.user.id, vote=False)
                new.save()

            # Return updated votes
            update.refresh_from_db()
            up = update.thumbsup
            down = update.thumbsdown

            return JsonResponse({'up': up, 'down': down})

    pass

