# -*- encoding: utf-8 -*-
from rest_framework import serializers
from app.models import *
from people.models import *
from places.models import *
from orders.models import *
from documents.models import *
from contracts.models import *

class EventTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventTypes
        fields = (
            'id',
            'type',
            'parent_id'
        )
class ContractorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contractors
        fields = (
            'id',
            'title',
            'type',
        )

class ContractorsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contractors
        fields = (
            'id',
            'contractor_title',
            'contractor_type', 'service_worker_type',
            'contractor_nearest_underground',
            'contractor_site', 'contractor_instagram',
            'contractor_from_recommendation', 'contractor_from_internet',
            'contractor_from_event',
            'contractor_cooperated',
            'contractor_is_moscow', 'contractor_moscow_region',
            'contractor_regions',
            'contractor_region', 'contractor_city', 'contractor_locality',
            'contractor_street', 'contractor_house_num', 'contractor_house_case',
            'contractor_house_entrance', 'contractor_floor', 'contractor_office',
            'contractor_address_note',
            'contractor_payment', 'contractor_prepayment', 'contractor_agency_payment',
            'contractor_service',
            'contractor_additional_service',
            'contractor_contact_person', 'contractor_contact_person_phone',
            'contractor_contact_note',
        )

class PlacesSerializer(serializers.ModelSerializer):
    place_type = serializers.StringRelatedField()

    class Meta:
        model = Places
        fields = (
            'id',
            'place_name',
            'place_type',
        )

class PlaceDetailSerializer(serializers.ModelSerializer):
    # halls = serializers.StringRelatedField(many=True)
    place_event_type = serializers.StringRelatedField(many=True)
    place_manager_name = serializers.StringRelatedField(many=True)
    place_сontractors = serializers.StringRelatedField(many=True)
    place_type = serializers.StringRelatedField()

    class Meta:
        model = Places
        fields = (
            'id',
            'place_name', 'place_type',
            'place_site', 'place_instagram',
            'halls',
            'place_event_type',
            'place_is_in_moscow', 'place_in_moscow_region',
            'place_in_regions',
            'place_nearest_undeground',
            'place_city', 'place_region', 'place_locality',
            'place_street', 'place_house_num', 'place_house_case',
            'place_house_entrance', 'place_floor', 'place_office',
            'place_address_note',
            'place_from_recommendation', 'place_from_internet',
            'place_from_event',
            'place_cooperated' ,
            'monday_to_tuesday',
            'friday', 'sunday', 'saturday',
            'accommodation_services',
            'accommodation_discount',
            'place_food_cost_banquet', 'place_food_cost_buffet',
            'is_kitchen', 'is_catering',
            'cork_fee',
            'cork_fee_note_yes', 'cork_fee_note_no',
            'alcohol',
            'alcohol_note_yes', 'alcohol_note_no',
            'dance_hall', 'scene',
            'sound',
            'sound_note_yes', 'sound_note_no', 'sound_note_perhaps',
            'light',
            'light_note_yes', 'light_note_no', 'light_note_perhaps',
            'technical_support',
            'additional_possibilities',
            'toilets_stationary', 'toilets_stationary_quantity',
            'toilets_mobility', 'toilets_mobility_quantity',
            'toilets_mobility_no',
            'toilets_mobility_perhaps',
            'parking_security', 'parking_security_quantity',
            'parking_security_no',
            'parking_security_is_cost', 'parking_security_cost',
            'parking_security_cost_no',
            'parking_security_quantity_places',
            'place_prepayment', 'place_agency_payment',
            'place_prepayment_order',
            'place_contact_person',
            'place_contact_person_phone', 'place_contact_person_email',
            'place_stage_negotiations_date', 'place_manager_name',
            'place_agreement', 'place_date_meeting',
            'place_stage_negotiations_note',
            'place_сontractors',
        )

class EmployersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employers
        fields = (
            'id',
            'employer_first_name',
            'employer_last_name',
        )

class EmployerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employers
        fields = (
            'id',
            'employer_first_name',
            'employer_last_name',
            'employer_date_birthday',
            'employer_avatar',
            'employer_post',
            'employer_city',
            'employer_visa',
        )

class ArtistsSerializer(serializers.ModelSerializer):
    artist_type = serializers.StringRelatedField()
    class Meta:
        model = Artists
        fields = (
            'id',
            'artist_name',
            'artist_type',
        )

class ArtistDetailSerializer(serializers.ModelSerializer):
    artist_type = serializers.StringRelatedField()
    artist_manager_name = serializers.StringRelatedField(many=True)

    class Meta:
        model = Artists
        fields = (
            'id',
            'artist_name',
            'artist_type',
            'artist_site', 'artist_instagram',
            'artist_from_recommendation', 'artist_from_internet',
            'artist_from_event',
            'artist_cooperated',
            'artist_is_in_moscow', 'artist_in_moscow_region',
            'artist_in_regions',
            'artist_city',
            'artist_region', 'artist_locality',
            'artist_street',
            'artist_house_num', 'artist_house_case',
            'artist_house_entrance', 'artist_floor',
            'artist_office',
            'artist_address_note',
            'artist_prepayment', 'artist_agency_payment',
            'artist_prepayment_order',
            'artist_contact_person',
            'artist_contact_person_phone', 'artist_contact_person_email',
            'artist_stage_negotiations_date',
            'artist_manager_name',
            'artist_agreement',
            'artist_date_meeting',
            'artist_stage_negotiations_note',
            'artist_date_performance',
        )

class VisaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visa
        fields = (
            'id',
            'visa_full_name_cyrillic',
        )

class VisaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visa
        fields = (
            'id',
            'visa_full_name_cyrillic',
            'visa_full_name_latin',
            'visa_sex',
            'visa_date_birthday',
            'visa_data_city',
            'visa_citizenship',
            'visa_father_name',
            'visa_mother_name',
            'visa_occupation',
            'visa_passport_number',
            'visa_passport_end',
            'visa_passport_city',
            'visa_hotel_address',
        )

class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers

        fields = (
            'id',
            'customer_full_name',
        )

class CustomerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers

        fields = (
            'id',
            'customer_full_name',
            'customer_phone',
            'customer_email',
            'customer_visa',
            'customer_account',
        )

class HallsSerializer(serializers.ModelSerializer):
    class Meta:
        models = Halls
        fields = ('hall_name',
                  'hall_footage',
                  'hall_people_quantity_banquet',
                  'hall_people_quantity_buffet',
                  'hall_year_round_check',
                  'hall_year_round_field')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        models = Event
        fields = (
            'id',
            'event_name',
        )

class EventDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'id',
            'event_name',
            'event_type',
            'event_date',
            'event_people_quantity',
            'event_wish',
            'event_places',
            'event_artists',
            'event_customers',
        )
class AdventuresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adventures
        fields = (
            'id',
            'adventure_number'
        )

class AdventureDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adventures
        fields = (
            'id',
            'adventure_number',
            'adventure_customer', 'adventure_employer',
            'adventure_transfer_there_arrival',
            'adventure_transfer_there_departure',
            'adventure_transfer_back_arrival',
            'adventure_transfer_back_departure',
            'adventure_by_yourself_there_arrival',
            'adventure_by_yourself_there_departure',
            'adventure_by_yourself_back_arrival',
            'adventure_by_yourself_back_departure',
            'adventure_accommodation_settlement',
            'adventure_accommodation_eviction',
            'adventure_room_type', 'adventure_room_number',
            'adventure_room_night_quantity',
            'adventure_room_additional_night_quantity',
            'adventure_room_additional_supplement',
        )

class PartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partners
        fields = (
            'id',
            'partner_name',
            'partner_phone',
            'partner_email',
            'partner_site',
            'partner_note',
        )

class BartersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barters
        fields = (
            'id',
            'barter_number',
        )

class BarterDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barters
        fields = (
            'id',
            'barter_number',
            'barter_date_start',
            'barter_date_expiration',
            'barter_artist',
            'barter_partner',
            'barter_contractor',
            'barter_manager',
        )
