from django.contrib import admin
from .models import ShortURL


@admin.register(ShortURL)
class ShortURLAdmin(admin.ModelAdmin):
    list_display = ('code', 'original_url', 'click_count', 'created_at')
    search_fields = ('code', 'original_url')
    readonly_fields = ('created_at', 'click_count')
