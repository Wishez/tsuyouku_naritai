# -*- encoding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from app.models import PlaceTypes, EventTypes
from people.models import Employers, Contractors
# Create your models here.
class Halls(models.Model):
    hall_name = models.CharField(_('Названия зала'),
                            max_length=400)
    hall_footage = models.DecimalField(_('Метраж Зала(квадратные метры)'),
                                       max_digits=1000,
                                       decimal_places=2,
                                       default=0.00)
    hall_people_quantity_banquet = models.IntegerField(_('Банкет'),
                                                  default=0)
    hall_people_quantity_buffet = models.IntegerField(_('Фуршет'),
                                                 default=0)
    hall_year_round_check = models.NullBooleanField(_('Круглогодично'))
    hall_year_round_field = models.CharField(_('Круглогодично'),
                                        max_length=200)

    def __str__(self):
        return self.hall_name
    class Meta:
        verbose_name = 'Зал'
        verbose_name_plural = 'Залы'
class Places(models.Model):
    place_name = models.CharField(_('Название площадки'),
                            max_length=200)
    # placeTypes = (
    #     (_('Банкеты'), 'Банкеты'),
    #     (_('Фуршеты'), 'Фуршеты'),
    #     (_('Рестораны'), 'Рестораны'),
    #     (_('Гостиницы'), 'Гостиницы'),
    #     (_('Отели'), 'Отели'),
    #     (_('Курорты'), 'Курорты'),
    #     (_('Кафе'), 'Кафе'),
    #     (_('Бары'), 'Бары'),
    #     (_('Шатры'), 'Шатры'),
    #     (_('Летние площадки'), 'Летние площадки'),
    #     (_('Открытые площадки'), 'Открытые площадки'),
    #     (_('Осабняки'), 'Осабняки'),
    #     (_('Дворцы'), 'Дворцы'),
    #     (_('Усадьбы'), 'Усадьбы'),
    #     (_('Развлекательные'), 'Развлекательные'),
    #     (_('Спортивные'), 'Спортивные'),
    #     (_('Игровые'), 'Игровые'),
    # )
    place_type = models.ForeignKey(PlaceTypes, verbose_name=_('Тип площадки'))
    place_site = models.URLField(_('Сайт площадки'),
                                 max_length=300,
                                 default='https://')
    place_instagram = models.URLField(_('Инстаграм'),
                                      max_length=300,
                                      default='https://www.instagram.com/')

    halls = models.ManyToManyField(Halls, verbose_name=_('Залы'))

    place_event_type = models.ManyToManyField(EventTypes, verbose_name=_('Тип мероприятия'))
    # event_type_another = models.CharField(_('Другой тип'),
    #                                       max_length=200,
    #                                       null=True,
    #                                       blank=True)
    place_is_in_moscow = models.BooleanField(
        _('Москва'),
        default=False
    )

    place_in_moscow_region = models.CharField(
        _('Московская область'),
        max_length=100,
        null=True,
        default=None,
        blank=True
    )
    place_in_regions = models.CharField(
        _('Регионы'),
        max_length=150,
        null=True,
        default=None,
        blank=True
    )

    place_nearest_undeground = models.CharField(_('Ближайшее метро'),
                                                max_length=150)

    place_region = models.CharField(
        _('Область'),
        max_length=100,
        null=True,
        blank=True
    )
    place_city = models.CharField(
        _('Город'),
        max_length=100,
    )
    place_locality = models.CharField(
        _('Населённый пункт'),
        max_length=150,
        blank=True,
        null=True
    )
    place_street = models.CharField(
        _('Улица'),
        max_length=150,
    )
    place_house_num = models.DecimalField(
        _('Дом'),
        max_digits=500,
        decimal_places=0,
        default=0
    )
    place_house_case = models.CharField(
        _('Корпус'),
        max_length=8,
    )
    place_house_entrance = models.DecimalField(
        _('Подъезд'),
        max_digits=1000,
        decimal_places=0,
        default=0
    )
    place_floor = models.DecimalField(
        _('Этаж'),
        max_digits=100,
        decimal_places=0,
        default=0
    )
    place_office = models.CharField(
        _('Офис'),
        max_length=150,
    )
    place_address_note = models.TextField(
        _('Примечание'),
        max_length=450,
    )
    place_from_recommendation = models.CharField(
        _('По рекомендации'),
        max_length=150,
        null=True,
        default=None
    )
    place_from_internet = models.CharField(
        _('Из интернета'),
        max_length=150,
        null=True,
        default=None
    )
    place_from_event = models.CharField(
        _('С мероприятия'),
        max_length=150,
        null=True,
        default=None
    )
    place_cooperated = models.NullBooleanField(
        _('Работали с ним или нет'),
        default=False
    )
    monday_to_tuesday = models.CharField(_('Понедельник - четверг'),
                                         max_length=100)
    friday = models.CharField(_('Пятница'),
                              max_length=100)
    saturday = models.CharField(_('Суббота'),
                              max_length=100)
    sunday = models.CharField(_('Воскресенье'),
                                max_length=100)
    accommodation_services = models.TextField(_('Что входит в Стоимость проживания'),
                                max_length=400)
    accommodation_discount = models.DecimalField(_('Скидка на проживание(%/руб)'),
                                                 max_digits=1000,
                                                 decimal_places=2,
                                                 default=0.00)
    place_food_cost_banquet = models.DecimalField(_('Банкета'),
                                                 max_digits=1000,
                                                 decimal_places=0,
                                                 default=0
                                                  )
    place_food_cost_buffet = models.DecimalField(_('Фуршета'),
                                                  max_digits=1000,
                                                  decimal_places=0,
                                                 default=0)
    is_kitchen = models.NullBooleanField(_('Собственная кухня'),
                                         default=False)
    is_catering = models.NullBooleanField(_('Можно-ли использовать свой кейтеринг'),
                                          default=False)
    cork_fee = models.NullBooleanField(_('Пробковый сбор'),
                                          default=False)
    cork_fee_note_yes = models.TextField(_('Примечание к "Да"'),
                                         max_length=400,
                                         null=True,
                                         blank=True)
    cork_fee_note_no = models.TextField(_('Примечание к "Нет"'),
                                        max_length=400,
                                        null=True,
                                        blank=True
                                        )

    alcohol = models.NullBooleanField(_('Свой Алкоголь'),
                                      default=False)
    alcohol_note_yes = models.TextField(_('Примечание к "Да"'),
                                        max_length=400,
                                        null=True,
                                        blank=True
                                        )
    alcohol_note_no = models.TextField(_('Примечание к "Нет"'),
                                       max_length=400,
                                       null=True,
                                       blank=True)
    # Equipment
    threePossibleTypes = (
        (_('Да'), 'Да'),
        (_('Нет'), 'Нет'),
        (_('Можно установить'), 'Можно установить')
    )
    dance_hall = models.CharField(_('Танцевальный зал'),
                                  choices=threePossibleTypes,
                                  max_length=20,
                                  default='Нет')

    scene = models.CharField(_('Сцена'),
                             choices=threePossibleTypes,
                             max_length=20,
                             default='Нет')

    sound = models.CharField(_('Звук'),
                             choices=threePossibleTypes,
                             max_length=20,
                             default='Нет')
    sound_note_yes = models.CharField(_('Примечание к "Да"'),
                                      max_length=400,
                                      null=True,
                                      blank=True)
    sound_note_no = models.CharField(_('Примечание к "Нет"'),
                                     max_length=400,
                                     null=True,
                                     blank=True)
    sound_note_perhaps = models.CharField(_('Примечание к "Можно установить"'),
                                     max_length=400,
                                     null=True,
                                     blank=True)

    light = models.CharField(_('Свет'),
                             choices=threePossibleTypes,
                             max_length=20,
                             default='Нет')
    light_note_yes = models.TextField(_('Примечание к "Да"'),
                                      max_length=300,
                                      null=True,
                                      blank=True)
    light_note_no = models.TextField(_('Примечание к "Нет"'),
                                     max_length=300,
                                     null=True,
                                     blank=True)
    light_note_perhaps = models.TextField(_('Примечание к "Можно установить"'),
                                          max_length=300,
                                          null=True,
                                          blank=True)
    technical_support = models.CharField(_('Техническое сопровождение входящее в стоимость'),
                                         max_length=300)
    additional_possibilities = models.CharField(_('Дополнительные возможности'),
                                                max_length=400)
    # Toilets
    toilets_stationary = models.NullBooleanField(_('Стационарные туалеты'),
                                                 default=False)
    toilets_stationary_quantity = models.IntegerField(_('Колличество стационарных туалетов'),
                                                      default=0)

    toilets_mobility = models.CharField(_('Мобилные туалеты'),
                                        choices=threePossibleTypes,
                                        max_length=20,
                                        default='Нет')
    toilets_mobility_quantity = models.IntegerField(_('Колличество мобилных туалетов'),
                                                    default=0)
    toilets_mobility_no = models.CharField(_('Примечание к "Нет"'),
                                           max_length=400,
                                           null=True,
                                           blank=True)
    toilets_mobility_perhaps = models.CharField(_('Примечание к "Можно установить"'),
                                                max_length=400,
                                                null=True,
                                                blank=True)
    #Parking
    parking_security = models.NullBooleanField(_('Охраняемая парковка'),
                                               default=False)
    parking_security_quantity = models.IntegerField(_('Колличество парковок на территории'),
                                                    default=0)
    parking_security_no = models.CharField(_('Примечание к "Нет"'),
                                           max_length=400,
                                           null=True,
                                           blank=True)

    parking_security_is_cost = models.NullBooleanField(_('Есть стоимость парковки'),
                                                       default=False)
    parking_security_cost = models.IntegerField(_('Стоимость парковки'),
                                                default=0)
    parking_security_cost_no = models.CharField(_('Примечание к "Нет" '),
                                                max_length=400,
                                                null=True,
                                                blank=True)
    parking_security_quantity_places = models.IntegerField(_('Колличество парковачных мест'),
                                                           default=0)
    # Payments
    place_prepayment = models.CharField(_('Предоплата'),
                                        max_length=50)
    place_prepayment_order = models.TextField(_('Порядок предоплаты'),
                                              max_length=100)
    place_agency_payment = models.IntegerField(_('Агентские %'),
                                                default=0)
    # Contact
    place_contact_person = models.CharField(
        _('Имя контактного лица'),
        max_length=150
    )
    place_contact_person_phone = PhoneNumberField(
        _('Телефон контактного лица'),
        max_length=24,
        default='+7'
    )
    place_contact_person_email = models.EmailField(_('Электронная почта'), max_length=120)
    # Negotiations
    place_stage_negotiations_date = models.DateField(_('Дата'),
                                                    default=timezone.now)
    place_manager_name = models.ManyToManyField(Employers,
                                          verbose_name=_('Имя Менеджера'))

    place_agreement = models.TextField(_('Результат договорённости'),
                                 max_length=400)

    place_date_meeting = models.DateTimeField(_('Дата и время следующего контакта/Встречи'))

    place_stage_negotiations_note = models.TextField(_('Примечание'),
                                                     max_length=400)

    place_сontractors = models.ManyToManyField(Contractors, verbose_name=_('Подрядчики'))

    def __str__(self):
        return self.place_name
    class Meta:
        verbose_name = 'Площадка'
        verbose_name_plural = 'Площадки'