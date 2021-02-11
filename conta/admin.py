from django.contrib import admin

from .models import Conta


class ContaAdmin(admin.ModelAdmin):

    list_display = ['conta']
    search_fields = ['conta']

admin.site.register(Conta, ContaAdmin)    