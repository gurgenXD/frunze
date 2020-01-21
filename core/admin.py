from django.contrib import admin
from core.models import Index, Advantage


admin.site.register(Advantage)

@admin.register(Index)
class IndexAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'phone', 'slogan', 'desc', 'about')
        }),
        ('SEO', {
            'fields': ('slug', 'seo_title', 'seo_desc', 'seo_kwrds'),
            'classes': ('grp-collapse grp-closed',),
        }),
    )

    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'phone', 'slogan')

    class Media:
        js = (
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',
        )