from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin
from core.models import *


admin.site.register(MailFromString)
admin.site.register(MailToString)


@admin.register(Index)
class IndexAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'phone', 'slogan', 'desc', 'about', 'document')
        }),
    )
    list_display = ('title', 'phone', 'slogan')

    class Media:
        js = (
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',
        )


admin.site.unregister(FlatPage)

@admin.register(FlatPage)
class ExtendedFlatPageAdmin(FlatPageAdmin):
    class Media:
        js = (
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',
        )

admin.site.register(Advantage)
admin.site.register(TitleTag)
