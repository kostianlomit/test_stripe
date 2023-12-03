from django.contrib import admin

from .models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name')



admin.site.register(Item, ItemAdmin)
admin.site.site_title = 'Админ-панель товаров'
