from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog'),
    path('<int:pk>', views.PostDetail.as_view(), name='post'),
    path('blog/search', views.search_venues, name='search-venues'),
    path('like/', views.like, name='like'),
    path('thumbs/', views.thumbs, name='thumbs'),
    path('<tag_slug>', views.TagList,name='post_list_by_tag'),
]