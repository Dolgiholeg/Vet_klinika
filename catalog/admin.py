from django.contrib import admin
from .models import *
admin.site.register(Poroda)
admin.site.register(Disease)
admin.site.register(Medicine)


class Klientadmin(admin.ModelAdmin):
    list_display = ('name','age','poroda','disease')
admin.site.register(Klient, Klientadmin)