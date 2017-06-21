# -*- encoding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from app.models import EventTypes
from places.models import Places
from people.models import Artists, Customers, Employers
# Create your models here.


class Event(models.Model):
    event_name = models.CharField(_('Название'), max_length=150)
    event_type = models.ManyToManyField(EventTypes, verbose_name=_('Тип'))
    event_date = models.DateField(_('Дата'))
    event_people_quantity = models.IntegerField(_('Колличество человек'))
    event_wish = models.TextField(_('Пожелание'), max_length=300)
    event_places = models.ManyToManyField(Places, verbose_name=_('Место проведения'))
    event_artists = models.ManyToManyField(Artists, verbose_name=_('Артисты'))
    event_customers = models.ManyToManyField(Customers, verbose_name=_('Менеджеры'))
    created_at = models.DateField(_('Дата создания'), auto_now_add=True)

    def __str__(self):
        return self.event_name

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

class Adventures(models.Model):

    adventure_number = models.CharField(_('Порядковы номер'), max_length=100,
                                        blank=True, null=True)
    adventure_customer = models.ForeignKey(Customers, verbose_name=_('Клиент'))
    adventure_employer = models.ForeignKey(Employers, verbose_name=_('Сотрудник'))
    adventure_transfer_there_arrival = models.DateTimeField(
        _('Трансфер туда - Время отбытия'),
        blank=True, null=True)
    adventure_transfer_there_departure = models.DateTimeField(
        _('Трансфер туда - Время прибытия'),
        blank=True, null=True)
    adventure_transfer_back_arrival = models.DateTimeField(
        _('Трасфер обратно - Время отбытия'),
        blank=True, null=True)
    adventure_transfer_back_departure = models.DateTimeField(
        _('Трасфер обратно - Время прибытия'),
        blank=True, null=True)
    adventure_by_yourself_there_arrival = models.DateTimeField(
        _('Самостоятельно туда - Время отбытия'),
        blank=True, null=True)
    adventure_by_yourself_there_departure = models.DateTimeField(
        _('Самостоятельно туда - Время прибытия'),
        blank=True, null=True)
    adventure_by_yourself_back_arrival = models.DateTimeField(
        _('Самостоятельно обратно - Время отбытия'),
        blank=True, null=True)
    adventure_by_yourself_back_departure = models.DateTimeField(
        _('Самостоятельно обратно - Время прибытия'),
        blank=True, null=True)

    adventure_accommodation_settlement = models.DateTimeField(
        _('Заселение'),
        blank=True, null=True)
    adventure_accommodation_eviction = models.DateTimeField(
        _('Выселение'),
        blank=True, null=True)

    roomTypes = (
        (_('SNGL'), 'SNGL'),
        (_('DBL'), 'DBL'),
        (_('TWN TRPL'), 'TWN TRPL'),
        (_('DE LUXE'), 'DE LUXE'),
        (_('Business'), 'Business'),
        (_('Apartment'), 'Apartment'),
        (_('President'), 'President'),
    )
    adventure_room_type = models.CharField(
        _('Тип номера'),
        choices=roomTypes,
        max_length=50
    )
    adventure_room_number = models.IntegerField(_('Номер комнаты'))
    adventure_room_night_quantity = models.IntegerField(_('Колличество ночей'))

    adventure_room_additional_night_quantity = models.IntegerField(_('Колличество ночей'))
    adventure_room_additional_supplement = models.DecimalField(
        _('Сумма доплаты'),
        max_digits=20,
        decimal_places=2)
    created_at = models.DateField(_('Дата создания'), auto_now_add=True)

    def __str__(self):
        return self.adventure_number

    class Meta:
        verbose_name = 'Путешествие'
        verbose_name_plural = 'Путешествия'