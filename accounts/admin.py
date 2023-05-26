from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomerUser

class CustomUserAdmin(UserAdmin):
    pass
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    # model = CustomerUser
    # list_display = ['email', 'username', 'age', 'is_staff',]
    # fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("name",)}),)
    # add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('name',)}),)
    
admin.site.register(CustomerUser,CustomUserAdmin)    


