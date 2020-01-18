from django.contrib import admin
from documents.models import Document


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'document', 'is_active', 'slug')
        }),
    )

    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'is_active', 'created')
    list_editable = ('is_active',)
    list_filter = ('is_active',)
    search_fields = ('title',)
