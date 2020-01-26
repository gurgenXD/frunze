from django.contrib import admin
from callback.models import CallBack


@admin.register(CallBack)
class CallBackAdmin(admin.ModelAdmin):
    list_display = ( 'phone', 'created')
