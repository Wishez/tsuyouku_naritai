# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import *
from mptt.admin import MPTTModelAdmin
# Register your models here.

class AdminEventTypes(MPTTModelAdmin):
    search_fields = ['type']
    list_display = ('type', 'parent')

admin.site.register(EventTypes, AdminEventTypes)
admin.site.register(PlaceTypes)
admin.site.register(ArtistTypes)
