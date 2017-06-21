# -*- encoding: utf-8 -*-
from rest_framework import viewsets
from .serializers import *

class EventTypesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EventTypes.objects.all()
    serializer_class = EventTypesSerializer

class ContractorsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Contractors.objects.all()
    serializer_class = ContractorsDetailSerializer
    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return ContractorsSerializer
    #     return ContractorsDetailSerializer

class PlacesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Places.objects.all()
    serializer_class = PlaceDetailSerializer
    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return PlacesSerializer
    #     return PlaceDetailSerializer

class EmployersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Employers.objects.all()
    serializer_class = EmployerDetailSerializer
    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return EmployersSerializer
    #     return EmployerDetailSerializer

class ArtistsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Artists.objects.all()
    serializer_class = ArtistDetailSerializer
    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return ArtistsSerializer
    #     return ArtistDetailSerializer

class VisaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Visa.objects.all()
    serializer_class = VisaDetailSerializer
    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return VisaSerializer
    #     return VisaDetailSerializer

class CustomersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustomerDetailSerializer
    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return CustomersSerializer
    #     return CustomerDetailSerializer

class HallsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Halls.objects.all()
    serializer_class = HallsSerializer

class EventsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer
    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return EventSerializer
    #     return EventDetailSerializer

class AdventuresViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Adventures.objects.all()
    serializer_class = AdventureDetailSerializer
    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return AdventuresSerializer
    #     return AdventureDetailSerializer

class PartnersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer

class BartersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Barters.objects.all()
    serializer_class = BarterDetailSerializer
    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return BartersSerializer
    #     return BarterDetailSerializer