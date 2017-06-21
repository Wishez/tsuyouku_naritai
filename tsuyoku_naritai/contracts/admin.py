# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import *

class AdminBarterModel(admin.ModelAdmin):
    search_fields = ('barter_number', 'barter_date_start', 'barter_date_expiration',)
    list_display = ('barter_number', 'barter_date_start', 'barter_date_expiration',)
    list_filter = ('barter_number', 'barter_artist',
                   'barter_partner', 'barter_contractor',
                   'barter_date_start', 'barter_date_expiration',)
    # filter_horizontal = ('barter_artist', 'barter_partner',
    #                      'barter_contractor', 'barter_contractor',)
    ordering = ('-barter_date_start',)
    data_hierarchy = 'barter_date_start'

    fieldsets = (
        (None, {
            'classes': ('grp-collapse grp-open'),
            'fields': (('barter_number',),)
        }),
        ('С кем заключается бартер', {
            'classes': ('grp-collapse grp-open'),
            'fields': (('barter_partner',),
                       ('barter_artist',),
                       ('barter_contractor',),)
        }),
        ('Заключающий бартер', {
            'classes': ('grp-collapse grp-open'),
            'fields': (('barter_manager',),)
        }),

    )

admin.site.register(Barters, AdminBarterModel)
