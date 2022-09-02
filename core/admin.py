from django.contrib import admin
from core.models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'read', 'created']
    list_filter = ['read', 'created',]
    search_fields = ['subject', 'name', 'created']