from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import userInformation
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('email','username','first_name','last_name','last_login','organizations')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined','last_login')
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
admin.site.register(userInformation, AccountAdmin)
