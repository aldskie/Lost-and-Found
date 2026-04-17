from django.contrib import admin
from .models import Account

# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstName', 'lastName', 'username', 'email', 'user_level')

admin.site.register(Account, AccountAdmin)