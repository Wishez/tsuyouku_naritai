# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import *
# Register your models here.
class AdminEventModel(admin.ModelAdmin):
    search_field = ('event_name',
                    'event_places', 'event_artists',
                    'event_customers',)
    list_display = ('event_name', 'event_date',)
    list_filter = ('event_name', 'event_date',
                   'event_places', 'event_artists',
                   'event_customers',)
    ordering = ('-created_at',)
    data_hierarchy = 'created_at'
    filter_horizontal = ('event_type', 'event_places',
                         'event_artists', 'event_customers',)
    fieldsets = (
        (None, {
            'classes': ('grp-collapse grp-open',),
            'fields': (('event_name',),
                       ('event_type',),
                       ('event_date', 'event_people_quantity',),
                       ('event_wish',),)
        }),
        (None, {
            'classes': ('grp-collapse grp-open',),
            'fields': (('event_places',),
                       ('event_artists',),
                       ('event_customers',),)
        }),
    )
class AdminAdventureModel(admin.ModelAdmin):
    search_field = ('adventure_number',)
    list_display = ('adventure_number', 'adventure_transfer_there_arrival',
                    'adventure_transfer_there_departure',
                    'adventure_transfer_back_arrival',
                    'adventure_transfer_back_departure',
                    'adventure_by_yourself_there_arrival',
                    'adventure_by_yourself_there_departure',
                    'adventure_by_yourself_back_arrival',
                    'adventure_by_yourself_back_departure',)
    list_filter = ('adventure_number', 'adventure_transfer_there_arrival',
                   'adventure_transfer_there_departure',
                    'adventure_transfer_back_arrival',
                    'adventure_transfer_back_departure',
                    'adventure_by_yourself_there_arrival',
                    'adventure_by_yourself_there_departure',
                    'adventure_by_yourself_back_arrival',
                    'adventure_by_yourself_back_departure',)
    ordering = ('-created_at',)
    data_hierarchy = 'created_at'

    fieldsets = (
        (None, {
            'fields': (('adventure_number',),
                       ('adventure_customer', 'adventure_employer',),)
        }),
        ('Трансфер', {
            'classes': ('grp-collapse grp-open',),
            'fields': (('adventure_transfer_there_arrival',),
                       ('adventure_transfer_there_departure',),
                       ('adventure_transfer_back_arrival',),
                       ('adventure_transfer_back_departure',),)
        }),
        ('Самостоятельно', {
            'classes': ('grp-collapse grp-open',),
            'fields': (('adventure_by_yourself_there_arrival',),
                       ('adventure_by_yourself_there_departure',),
                       ('adventure_by_yourself_back_arrival',),
                       ('adventure_by_yourself_back_departure',),)
        }),
        ('Проживание', {
            'classes': ('grp-collapse grp-open',),
            'fields': (('adventure_accommodation_settlement',
                        'adventure_accommodation_eviction',),
                       ('adventure_room_type', 'adventure_room_number',
                        'adventure_room_night_quantity',),)
        }),
        ('Доплата самостоятельно', {
            'classes': ('grp-collapse grp-open',),
            'fields': (('adventure_room_additional_night_quantity',
                        'adventure_room_additional_supplement',),)
        }),
    )
admin.site.register(Event, AdminEventModel)
admin.site.register(Adventures, AdminAdventureModel)
