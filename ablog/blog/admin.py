from django.contrib import admin
from .models import Post, Comment, Vote
from mptt.admin import MPTTModelAdmin
# Register your models here.
class CommentInLine(admin.StackedInline):
    model = Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author','image', 'publish','status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    # inlines = [CommentInLine]
admin.site.register(Post, PostAdmin)

# admin.site.register(Comment)
    
admin.site.register(Comment, MPTTModelAdmin)
admin.site.register(Vote)

# class MyModelAdmin(admin.ModelAdmin):
#     list_display = ['tag_list']

#     def get_queryset(self, request):
#         return super().get_queryset(request).prefetch_related('tags')

#     def tag_list(self, obj):
#         return u", ".join(o.name for o in obj.tags.all())