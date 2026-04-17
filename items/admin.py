from django.contrib import admin
from .models import ItemDetails

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_name', 'item_location', 'item_category', 'item_status', 'item_date_and_time', 'item_image')

admin.site.register(ItemDetails, ItemAdmin)