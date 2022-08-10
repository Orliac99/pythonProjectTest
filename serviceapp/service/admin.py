from django.contrib import admin
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'numero', 'type_service', 'tarifs',)
    search_fields = ['nom']

# Register your models here.
admin.site.register(Service, ServiceAdmin)
