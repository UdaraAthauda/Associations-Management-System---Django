from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']
    search_fields = ['id', 'username']


admin.site.register(Association)
admin.site.register(AssociationMember)
admin.site.register(Service)
admin.site.register(ServiceRequest)
