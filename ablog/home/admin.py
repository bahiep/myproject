from .models import Shop, Withdraw
from django.contrib import admin

# Register your models here.
class HomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','body','image', 'publish')
    list_filter = ('publish', 'author')
    search_fields = ('title', 'body')
    # prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['publish']
    # inlines = [CommentInLine]
admin.site.register(Shop, HomeAdmin)

class WithdrawAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'author','bankname','accountnumber','status', 'publish')
    # list_filter = ('publish', 'author')
    # search_fields = ('title', 'body')
    # # prepopulated_fields = {'slug': ('title',)}
    # # raw_id_fields = ('author',)
    # date_hierarchy = 'publish'
    # ordering = ['publish']
    # inlines = [CommentInLine]
admin.site.register(Withdraw, WithdrawAdmin)