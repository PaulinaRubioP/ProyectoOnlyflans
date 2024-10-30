from django.contrib import admin
from .models import Flan, Contact

@admin.register(Flan)
class FlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_private', 'rating', 'flan_uuid')  # Agregamos 'rating' a list_display
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at')
    search_fields = ('name', 'email')
