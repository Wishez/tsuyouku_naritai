# -*- encoding: utf-8 -*-
from .models import *
from django.contrib import admin
# Register your models here.
class AdminPlaceModel(admin.ModelAdmin):
    list_display = ('place_name',
                     'place_type',
                     'place_contact_person',
                     'place_contact_person_phone',
                     'place_contact_person_email',)
    search_fields = ('place_name',
                     'place_type',
                     'place_event_type',
                     'place_city')
    list_filter = ('place_type', 'place_name', 'place_stage_negotiations_date')
    ordering = ('-place_stage_negotiations_date',)
    date_hierarchy = 'place_stage_negotiations_date'
    filter_horizontal = ('halls', 'place_event_type',
                         'place_manager_name', 'place_сontractors',)
    fieldsets = (
        (None, {
           'classes': ('',),
           'fields': (('place_name', 'place_type',),
                      ('place_site', 'place_instagram'),
                      ('halls',),
                      ('place_event_type',),
                      ('place_is_in_moscow', 'place_in_moscow_region'),
                      ('place_in_regions',),
                      ('place_nearest_undeground',),)
        }),
        ('Адрес', {
            'classes': ('grp-collapse grp-open',),
            'fields': (('place_city',),
                       ('place_region', 'place_locality',),
                       ('place_street',),
                       ('place_house_num', 'place_house_case',),
                       ('place_house_entrance', 'place_floor',),
                       ('place_office',),
                       ('place_address_note',),)
        }),
        ('Источник откуда он', {
            'classes': ('grp-collapse grp-open',),
            'fields': (('place_from_recommendation', 'place_from_internet',),
                       ('place_from_event',),
                       ('place_cooperated'),)
        }),
        ('Прожиточная стоимость на человека', {
            'classes': ('grp-collapse grp-open',),
            'fields': (('monday_to_tuesday',),
                       ('friday', 'saturday',),
                       ('sunday',),
                       ('accommodation_services',),
                       ('accommodation_discount',),)
        }),
        ('Стоимость питания на человека', {
            'classes': ('grp-collapse grp-open',),
            'fields': (('place_food_cost_banquet', 'place_food_cost_buffet',),
                       ('is_kitchen', 'is_catering',),)
        }),
        ('Алкоголь', {
            'classes': ('grp-collapse grp-open',),
            'fields': (('cork_fee',),
                       ('cork_fee_note_yes',),
                       ('cork_fee_note_no',),
                       ('alcohol',),
                       ('alcohol_note_yes',),
                       ('alcohol_note_no'),)
        }),
        ('Специализированные помещения', {
            'classes': ('grp-collapse grp-open',),
            'fields': (('dance_hall', 'scene',),)
        }),
        ('Техническая экипировка', {
            'classes': ('grp-collapse grp-open',),
            'fields': (('sound',),
                       ('sound_note_yes',),
                       ('sound_note_no',),
                       ('sound_note_perhaps',),
                       ('light',),
                       ('light_note_yes',),
                       ('light_note_no',),
                       ('light_note_perhaps',),
                       ('technical_support',),
                       ('additional_possibilities',),)
        }),
        ('Туалеты', {
            'classes': ('grp-collapse grp-open',),
            'fields': (('toilets_stationary', 'toilets_stationary_quantity'),
                       ('toilets_mobility', 'toilets_mobility_quantity',),
                       ('toilets_mobility_no',),
                       ('toilets_mobility_perhaps',),)
        }),
        ('Парковка', {
            'classes': ('grp-collapse grp-open',),
            'fields': (('parking_security', 'parking_security_quantity',),
                       ('parking_security_no',),
                       ('parking_security_is_cost', 'parking_security_cost',),
                       ('parking_security_cost_no',),
                       ('parking_security_quantity_places',),)
        }),
        ('Оплата', {
            'classes': ('grp-collapse grp-open',),
            'fields': (('place_prepayment', 'place_agency_payment',),
                       ('place_prepayment_order',),)
        }),
        ('Контактное лицо', {
            'classes': ('grp-collapse grp-open',),
            'fields': (('place_contact_person',),
                       ('place_contact_person_phone', 'place_contact_person_email',),)
        }),
        ('Переговоры', {
            'classes': ('grp-collapse grp-open',),
            'fields': (('place_stage_negotiations_date',),
                       ('place_manager_name',),
                       ('place_agreement',),
                       ('place_date_meeting',),
                       ('place_stage_negotiations_note',),)
        }),
        ('Список подрядчиков', {
            'classes': ('grp-collapse grp-open',),
            'fields': (('place_сontractors',),)
        }),
    )
admin.site.register(Halls)
admin.site.register(Places, AdminPlaceModel)
