from django.contrib import admin
from products.models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('category', 'subcategory', 'title', 'article', 'price', 'desc', 'is_active')
        }),
        ('SEO', {
            'fields': ('slug', 'seo_title', 'seo_desc', 'seo_kwrds'),
            'classes': ('grp-collapse grp-closed',),
        }),
    )

    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'subcategory', 'article', 'price', 'is_active', 'created', 'updated')
    list_editable = ('is_active', 'price')
    list_filter = ('is_active', 'category__title', 'subcategory__title')
    search_fields = ('title', 'category__title', 'subcategory__title', 'article')

    class Media:
        js = (
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',
            '/static/js/back.js',
        )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'is_active')
        }),
        ('SEO', {
            'fields': ('slug', 'seo_title', 'seo_desc', 'seo_kwrds'),
            'classes': ('grp-collapse grp-closed',),
        }),
    )

    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('is_active',)
    search_fields = ('title',)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('category', 'title', 'is_active')
        }),
        ('SEO', {
            'fields': ('slug', 'seo_title', 'seo_desc', 'seo_kwrds'),
            'classes': ('grp-collapse grp-closed',),
        }),
    )

    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('is_active', 'category__title')
    search_fields = ('title', 'category__title')
