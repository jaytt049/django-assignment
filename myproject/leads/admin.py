from django.contrib import admin
from .models import Lead

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'status', 'created_by')
    search_fields = ('name', 'email')
    list_filter = ('status',)