from django.contrib import admin
from .models import Maqola, Category,Number


class MaqolaAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'update_at', 'author')
    list_display_links = ('category',)
    list_editable = ('title', 'author')
    search_fields = ('author',)

admin.site.register(Maqola, MaqolaAdmin)
admin.site.register(Category)
admin.site.register(Number)