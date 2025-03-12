from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']
    search_fields = ['id', 'username']

@admin.register(Association)
class AssociationAdmin(admin.ModelAdmin):
    search_fields = ['AssociationName']

@admin.register(AssociationMember)
class AssociationMemberAdmin(admin.ModelAdmin):
    search_fields = ['id', 'user__username', 'association__AssociationName']
    list_filter = ['adminAccept']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    search_fields = ['serviceTitle', 'association__AssociationName']

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    search_fields = ['user__username', 'service__association', 'service__serviceTitle']
    list_filter = ['status']

@admin.register(UserFeedbacks)
class UserFeedbacksAdmin(admin.ModelAdmin):
    list_filter = ['association__AssociationName', 'reply']


