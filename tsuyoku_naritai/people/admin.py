# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import *

class AdminContractorModel(admin.ModelAdmin):
    search_field = ['contractor_title', 'contractor_contact_person',
                    'service_worker_type', 'contractor_type',
                    'contractor_city']
    list_display = ('contractor_title', 'contractor_type', 'contractor_contact_person',
                    'contractor_contact_person_phone',)
    list_filter = ('contractor_type', 'contractor_title', 'contractor_contact_person')
    fieldsets = (
        (None, {
          'classes': ('',),
          'fields': (('contractor_title',),
                     ('contractor_type', 'service_worker_type'),
                     ('contractor_nearest_underground',),
                     ('contractor_site', 'contractor_instagram'),
          )
        }),

        ('Откуда он', {
            'classes': ('grp-collapse grp-open',),
            'fields': (('contractor_from_recommendation', 'contractor_from_internet',),
                       ('contractor_from_event',),
                       ('contractor_cooperated',),
            )
        }),
        ('Регион', {
            'classes': ('grp-collapse grp-open',),
            'fields': (('contractor_is_moscow', 'contractor_moscow_region',),
                       ('contractor_regions'),)
        }),
        ('Адрес', {
            'classes': ('grp-collapse grp-open',),
            'fields': (('contractor_city',),
                       ('contractor_region', 'contractor_locality',),
                       ('contractor_street',),
                       ('contractor_house_num', 'contractor_house_case',),
                       ('contractor_house_entrance', 'contractor_floor',),
                       ('contractor_office',),
                       ('contractor_address_note',),
            )
        }),
        ('Оплата', {
            'classes': ('grp-collapse grp-open',),
            'fields': (('contractor_payment', 'contractor_prepayment',),
                       ('contractor_agency_payment',),
                       ('contractor_service',),
                       ('contractor_additional_service',),
           )
        }),
        ('Контактное лицо', {
            'classes': ('grp-collapse grp-open',),
            'fields': (('contractor_contact_person', 'contractor_contact_person_phone',),
                        ('contractor_contact_note',),
             )
        }),
    )
class AdminEmployerModel(admin.ModelAdmin):
    search_fields = ('employer_first_name',
                     'employer_last_name', 'employer_post', 'employer_visa',)
    list_display = ('employer_first_name', 'employer_last_name',
                    'employer_post', 'employer_visa',)
    list_filter = ('employer_first_name', 'employer_last_name',
                   'employer_post', 'employer_visa', 'employer_number',)
class AdminArtistModel(admin.ModelAdmin):
    search_fields = ('artist_name',
                     'artist_type',
                     'artist_date_performance')
    list_filter = ('artist_name',
                   'artist_type',
                   'artist_date_performance')
    ordering = ('-artist_date_performance',)
    date_hierarchy = 'artist_date_performance'
    list_display = ('artist_name',
                    'artist_type',
                    'artist_contact_person',
                    'artist_contact_person_phone',
                    'artist_contact_person_email',
                    'artist_date_performance')
    filter_horizontal = ('artist_manager_name',)
    fieldsets = (
        # (None, {
        #     'classes': ('grp-collapse grp-open'),
        #     'fields': (('',),)
        # }),
        (None, {
            'fields': (('artist_name',),
                       ('artist_type'),
                       ('artist_site', 'artist_instagram',),)
        }),
        ('Откуда он', {
            'classes': ('grp-collapse grp-open',),
            'fields': (('artist_from_recommendation', 'artist_from_internet',),
                       ('artist_from_event',),
                       ('artist_cooperated',),)
        }),
        ('Регион', {
            'classes': ('grp-collapse grp-open',),
            'fields': (('artist_is_in_moscow', 'artist_in_moscow_region',),
                       ('artist_in_regions',),)
        }),
        ('Адрес', {
            'classes': ('grp-collapse grp-open',),
            'fields': (('artist_city',),
                       ('artist_region', 'artist_locality',),
                       ('artist_street',),
                       ('artist_house_num', 'artist_house_case',),
                       ('artist_house_entrance', 'artist_floor',),
                       ('artist_office',),
                       ('artist_address_note',),)
        }),
        ('Оплата', {
            'classes': ('grp-collapse grp-open',),
            'fields': (('artist_prepayment', 'artist_agency_payment',),
                       ('artist_prepayment_order',),)
        }),
        ('Контактное лицо', {
            'classes': ('grp-collapse grp-open',),
            'fields': (('artist_contact_person',),
                       ('artist_contact_person_phone', 'artist_contact_person_email',),)
        }),
        ('Переговоры', {
            'classes': ('grp-collapse grp-open',),
            'fields': (('artist_stage_negotiations_date',),
                       ('artist_manager_name',),
                       ('artist_agreement',),
                       ('artist_date_meeting',),
                       ('artist_stage_negotiations_note',),
                       ('artist_date_performance',),)
        }),
    )
class AdminCustomerModel(admin.ModelAdmin):
    search_fields = ('customer_full_name',)
    list_display = ('customer_full_name', 'customer_phone',
                    'customer_email', 'customer_account',)
    list_filter = ('customer_full_name', 'customer_account',)
class AdminPartnerModel(admin.ModelAdmin):
    search_field = ('partner_name',)
    list_display = ('partner_name', 'partner_phone',
                    'partner_email', 'partner_site',)
    list_filter = ('partner_name',)

admin.site.register(Customers, AdminCustomerModel)
admin.site.register(Employers, AdminEmployerModel)
admin.site.register(Artists, AdminArtistModel)
admin.site.register(Contractors, AdminContractorModel)
admin.site.register(Partners, AdminPartnerModel)
