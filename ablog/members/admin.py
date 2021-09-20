from django.contrib import admin
from .models import Bill, Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo', 'cash']
admin.site.register(Profile, ProfileAdmin)

class BillAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','image', 'publish')
    list_filter = ('publish', 'author')
    search_fields = ('title', 'body')
    # prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ('author',)
    # date_hierarchy = 'publish'
    ordering = ['publish']
    # inlines = [CommentInLine]
admin.site.register(Bill, BillAdmin)