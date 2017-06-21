# -*- encoding: utf-8 -*-
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r'event_types', EventTypesViewSet, 'event_types')
router.register(r'contractors', ContractorsViewSet, 'contractors')
router.register(r'places', PlacesViewSet, 'places')
router.register(r'employers', EmployersViewSet, 'employers')
router.register(r'artists', ArtistsViewSet, 'artists')
router.register(r'visa', VisaViewSet, 'visa')
router.register(r'customers', CustomersViewSet, 'customers')
router.register(r'halls', HallsViewSet, 'halls')
router.register(r'events', EventsViewSet, 'events')
router.register(r'adventures', AdventuresViewSet, 'adventures')
router.register(r'partners', PartnersViewSet, 'partners')
router.register(r'barters', BartersViewSet, 'barters')

urlpatterns = router.urls
