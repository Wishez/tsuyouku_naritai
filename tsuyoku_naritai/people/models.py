# -*- encoding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from app.models import ArtistTypes
from documents.models import Visa

class Employers(models.Model):
    employer_number = models.CharField(_('Порядковый номер'), max_length=100,
                                       blank=True, null=True)

    employer_first_name = models.CharField(_('Имя'), max_length=200)
    employer_last_name = models.CharField(_('Фамилия'), max_length=200)
    employer_date_birthday = models.DateField(_('Дата рождения'))

    employer_avatar = models.FileField(_('Фото'), upload_to='employer_avatars/')
    employer_post = models.CharField(_('Должность'), max_length=200)
    employer_city = models.CharField(_('Город'), max_length=200)

    employer_visa = models.ForeignKey(
        Visa,
        verbose_name=_('Виза сотрудника'),
        blank=True,
        null=True)

    employer_account = models.OneToOneField(
        'auth.User',
        verbose_name=_('Аккаунт сотрудника'),
        unique=True,
        blank=True,
        null=True)

    def __str__(self):
        return self.employer_first_name + '\t' + self.employer_last_name
    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
class Artists(models.Model):
    artist_name = models.CharField(_('Название группы/Имя артиста'),
                                   max_length=200)
    artist_type = models.ForeignKey(ArtistTypes, verbose_name=_('Тип артиста'), default=None)

    artist_site = models.URLField(_('Сайт площадки'),
                                  max_length=300,
                                  default='https://')
    artist_instagram = models.URLField(_('Инстаграм'),
                                       max_length=300,
                                       default='https://www.instagram.com/')
    artist_from_recommendation = models.CharField(
        _('По рекомендации'),
        max_length=150,
        null=True,
        default=None
    )
    artist_from_internet = models.CharField(
        _('Из интернета'),
        max_length=150,
        null=True,
        default=None
    )
    artist_from_event = models.CharField(
        _('С мероприятия'),
        max_length=150,
        null=True,
        default=None
    )
    artist_cooperated = models.NullBooleanField(
        _('Работали с ним или нет'),
        default=False
    )
    artist_is_in_moscow = models.BooleanField(
        _('Москва'),
        default=False
    )

    artist_in_moscow_region = models.CharField(
        _('Московская область'),
        max_length=100,
        null=True,
        default=None,
        blank=True
    )
    artist_in_regions = models.CharField(
        _('Регионы'),
        max_length=150,
        null=True,
        default=None,
        blank=True
    )
    artist_region = models.CharField(
        _('Область'),
        max_length=100,
        null=True,
        blank=True
    )
    artist_city = models.CharField(
        _('Город'),
        max_length=100,
    )
    artist_locality = models.CharField(
        _('Населённый пункт'),
        max_length=150,
        blank=True,
        null=True
    )
    artist_street = models.CharField(
        _('Улица'),
        max_length=150,
    )
    artist_house_num = models.DecimalField(
        _('Дом'),
        max_digits=500,
        decimal_places=0,
        default=0
    )
    artist_house_case = models.CharField(
        _('Корпус'),
        max_length=8,
    )
    artist_house_entrance = models.DecimalField(
        _('Подъезд'),
        max_digits=1000,
        decimal_places=0,
        default=0
    )
    artist_floor = models.DecimalField(
        _('Этаж'),
        max_digits=100,
        decimal_places=0,
        default=0
    )
    artist_office = models.CharField(
        _('Офис'),
        max_length=150,
    )
    artist_address_note = models.TextField(
        _('Примечание'),
        max_length=450,
    )

    artist_prepayment = models.CharField(_('Предоплата'),
                                        max_length=50)
    artist_prepayment_order = models.TextField(_('Порядок предоплаты'),
                                              max_length=100)
    artist_agency_payment = models.IntegerField(_('Агентские %'),
                                               default=0)
    # Contact
    artist_contact_person = models.CharField(
        _('Имя контактного лица'),
        max_length=150
    )
    artist_contact_person_phone = PhoneNumberField(
        _('Телефон контактного лица'),
        max_length=24,
        default='+7'
    )
    artist_contact_person_email = models.EmailField(_('Электронная почта'), max_length=120)
    # Negotiations
    artist_stage_negotiations_date = models.DateField(_('Дата'),
                                                     default=timezone.now)
    artist_manager_name = models.ManyToManyField(Employers,
                                                verbose_name=_('Имя Менеджера'))

    artist_agreement = models.TextField(_('Результат договорённости'),
                                       max_length=400)

    artist_date_meeting = models.DateTimeField(_('Дата и время следующего контакта/Встречи'))

    artist_stage_negotiations_note = models.TextField(_('Примечание'),
                                                     max_length=400)

    artist_date_performance = models.DateTimeField(_('Дата и время выступления'))

    def __str__(self):
        return self.artist_name
    class Meta:
        verbose_name = 'Артист'
        verbose_name_plural = 'Артисты'
class Contractors(models.Model):
    contractor_title = models.CharField(_('Название'), max_length=100)
    types = (
        (_('Техническое соправождение'), 'Техническое соправождение(Свет/Звук)'),
        (_('Оборудование/Декорации'), 'Оборудование - Декорации'),
        (_('Кейтринг'), 'Кейтринг'),
        (_('Транспорт'), 'Транспорт(Авто)'),
        (_('Декор/Оформление/Цветы'), 'Декор - Оформление - Цветы'),
        (_('Монтаж'), 'Монтаж (Фото/Видео)'),
        (_('Торты/Сладкое'), 'Торты - Сладкое'),
        (_('Полиграфия/Сувенирка'), 'Полиграфия - Сувенирка'),
        (_('Наемный персонал'), 'Наемный персонал'),
        (_('Стилисты/Визажисты'), 'Стилисты - Визажисты'),
    )
    contractor_type = models.CharField(_('Тип Подрядчика'),
                            choices=types,
                            max_length=50,
                            default='TCHHD'
                            )

    serviceWorkersTypes = (
        (_('Клининговые службы'), 'Клининговые службы'),
        (_('Грузчики'), 'Грузчики'),
        (_('Промышленные альпинисты'), 'Промышленные альпинисты'),
        (_('Промо-персонал'), 'Промо-персонал'),
        (_('Монтажники'), 'Монтажники'),
        (_('Организация парковки'), 'Организация парковки / парковщики'),
        (_('Хостес'), 'Модели на мерпориятие / Хостес'),
        (_('Охрана'), 'Охрана'),
        (_('Официанты'), 'Официанты'),
        (_('Бармены'), 'Бармены'),
    )
    service_worker_type = models.CharField(
        _('Тип наёмного персонала'),
        choices=serviceWorkersTypes,
        max_length=50,
        null=True,
        default=None,
        blank=True
    )

    contractor_nearest_underground = models.CharField(_('Ближайшее метро'), max_length=100)
    contractor_site = models.URLField(
        _('Сайт'),
        max_length=150,
        default='https://')
    contractor_instagram = models.URLField(
        _('Инстаграм'),
        max_length=150,
        default='https://www.instagram.com/')

    contractor_from_recommendation = models.BooleanField(
        _('Пришёл по рекомендации'),
        default=False
    )
    contractor_from_internet = models.BooleanField(
        _('Пришёл через интернет'),
        default=False
    )
    contractor_from_event = models.CharField(
        _('Пришёл с мероприятия'),
        max_length=150,
        null=True,
        blank=True
    )

    contractor_cooperated = models.NullBooleanField(
        _('Работали прежде или нет'),
        default=False
    )

    contractor_is_moscow = models.BooleanField(
        _('Москва'),
        default=False
    )

    contractor_moscow_region = models.CharField(
        _('Московская область'),
        max_length=100,
        null=True,
        default=None,
        blank=True
    )
    contractor_regions = models.CharField(
        _('Регионы'),
        max_length=150,
        null=True,
        default=None,
        blank=True
    )
    contractor_payment = models.IntegerField(
        _('Стоимость'),
        default=0
    )
    contractor_service = models.TextField(
        _('Что входит в стоимость'),
        max_length=1000
    )
    contractor_additional_service = models.CharField(
        _('Дополнительные услуги'),
        max_length=350,
        null=True,
        blank=True
    )
    contractor_prepayment = models.CharField(
        _('Предоплата'),
        max_length=12
    )
    contractor_agency_payment = models.CharField(
        _('Агенские %'),
        max_length=150,
        null=True,
        default=0
    )
    contractor_contact_person = models.CharField(
        _('Имя контактного лица'),
        max_length=150
    )
    contractor_contact_person_phone = PhoneNumberField(
        _('Телефон контактного лица'),
        max_length=24,
        default='+7'
    )
    contractor_contact_note = models.TextField(
        _('Примечание'),
        max_length=450,
    )

    contractor_region = models.CharField(
        _('Область'),
        max_length=100,
        null=True,
        blank=True
    )
    contractor_city = models.CharField(
        _('Город'),
        max_length=100,
    )
    contractor_locality = models.CharField(
        _('Населённый пункт'),
        max_length=150,
        blank=True,
        null=True
    )
    contractor_street = models.CharField(
        _('Улица'),
        max_length=150,
    )
    contractor_house_num = models.DecimalField(
        _('Дом'),
        max_digits=500,
        decimal_places=0,
        default=0
    )
    contractor_house_case = models.CharField(
        _('Корпус'),
        max_length=8,
        default='2A'
    )
    contractor_house_entrance = models.DecimalField(
        _('Подъезд'),
        max_digits=1000,
        decimal_places=0,
        default=0
    )
    contractor_floor = models.DecimalField(
        _('Этаж'),
        max_digits=100,
        decimal_places=0,
        default=0
    )
    contractor_office = models.CharField(
        _('Офис'),
        max_length=150,
    )
    contractor_address_note = models.TextField(
        _('Примечание'),
        max_length=450,
    )

    def __str__(self):
        return self.contractor_title
    class Meta:
        verbose_name = 'Подрядчик'
        verbose_name_plural = 'Подрядчики'
class Customers(models.Model):
    customer_full_name = models.CharField(_('ФИО'),
                                          max_length=300)

    customer_phone = PhoneNumberField(_('Телефон'),
                                             max_length=24,
                                             default='+7')
    customer_email = models.EmailField(_('E-mail'),
                                       max_length=150)
    customer_visa = models.ForeignKey(
        Visa,
        verbose_name=_('Виза клиента'),
        blank=True,
        null=True)

    customer_account = models.OneToOneField(
        'auth.User',
        verbose_name=_('Аккаунт клиента'),
        unique=True,
        blank=True,
        null=True)

    def __str__(self):
        return self.customer_full_name
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
class Partners(models.Model):
    partner_name = models.CharField(_('Имя'), max_length=150,)
    partner_phone = PhoneNumberField(
        _('Телефон'),
        max_length=24,
        default='+7'
    )
    partner_email = models.EmailField(
        _('Email'),
        max_length=100
    )
    partner_site = models.URLField(
        _('Сайт'),
        max_length=200
    )

    partner_note = models.TextField(_('Примечание'), max_length=300,
                                    blank=True, null=True)
    def __str__(self):
        return self.partner_name
    class Meta:
        verbose_name = 'Партнёр'
        verbose_name_plural = 'Партнёры'
