# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import *
# Register your models here.
class AdminVisaModel(admin.ModelAdmin):
    search_fields = ('visa_full_name_cyrillic', 'visa_data_city')
    list_display = ('visa_full_name_cyrillic', 'visa_date_birthday', 'visa_passport_number',)
    list_filter = ('visa_full_name_cyrillic', 'visa_sex', 'visa_passport_number',)

admin.site.register(Visa, AdminVisaModel)