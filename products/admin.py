from django.contrib import admin
from products.models import *


class CharacteristicInline(admin.TabularInline):
    model = Characteristic
    extra = 0
    classes = ('grp-collapse grp-closed',)


class OptionInline(admin.TabularInline):
    model = Option
    extra = 0
    fk_name = 'product'
    classes = ('grp-collapse grp-closed',)


class ImageInline(admin.TabularInline):
    model = Image
    extra = 0
    classes = ('grp-collapse grp-closed',)


class BarTypeInline(admin.TabularInline):
    model = BarType
    extra = 0
    classes = ('grp-collapse grp-closed',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('category', 'subcategory', 'title', 'article', 'price', 'in_stock', 'desc', 'is_active')
        }),
        ('SEO', {
            'fields': ('slug', 'seo_title', 'seo_desc', 'seo_kwrds'),
            'classes': ('grp-collapse grp-closed',),
        }),
    )

    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'subcategory', 'article', 'price', 'in_stock', 'is_active', 'created', 'updated')
    list_editable = ('is_active', 'price', 'in_stock')
    list_filter = ('is_active', 'category__title', 'subcategory__title')
    search_fields = ('title', 'category__title', 'subcategory__title', 'article')
    inlines = (ImageInline, CharacteristicInline, OptionInline, BarTypeInline)

    class Media:
        js = (
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',
            '/static/js/my-admin.js',
        )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title',)
        }),
        ('SEO', {
            'fields': ('slug', 'seo_title', 'seo_desc', 'seo_kwrds'),
            'classes': ('grp-collapse grp-closed',),
        }),
    )

    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('category', 'title',)
        }),
        ('SEO', {
            'fields': ('slug', 'seo_title', 'seo_desc', 'seo_kwrds'),
            'classes': ('grp-collapse grp-closed',),
        }),
    )

    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category',)
    list_filter = ('category__title',)
    search_fields = ('title', 'category__title')
