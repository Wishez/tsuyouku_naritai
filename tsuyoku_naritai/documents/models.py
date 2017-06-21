# -*- encoding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Visa(models.Model):
    visa_full_name_cyrillic = models.CharField(_('Full name (Cyrillic transcription)/ФИО (Кириллическая транскрипция)'),
                                    max_length=300,
                                    default='Гарри Поттер Эванс Верес')
    visa_full_name_latin = models.CharField(_('Full name(Latin transcription)/ФИО (Латинская транскрипция)'),
                                            max_length=300,
                                            default='Albus Persival Wulfric Brayan Damboldor')
    sex = (
        (_('Мужской/Male'), 'Мужской/Male'),
        (_('Женский/Female'), 'Женский/Female'),
    )
    visa_sex = models.CharField(_('Пол'),
                                max_length=50,
                                choices=sex,
                                default=_('Мужской/Male'))

    visa_date_birthday = models.DateField(_('Date of birth/Дата рождения'))
    visa_data_city = models.CharField(_('Place of birth/Место рождения'),
                                          max_length=150)
    visa_citizenship = models.CharField(_('Nationality/Гражданство'),
                                          max_length=150)
    visa_father_name = models.CharField(_('Father\'s name/Имя отца'),
                                       max_length=200)
    visa_mother_name = models.CharField(_('Mother\'s name/Имя матери'),
                                       max_length=200)

    visa_occupation = models.CharField(_('Occupation/Место работы и должность'),
                                        max_length=400)

    visa_passport_number = models.IntegerField(_('Passport number/Номер загран-паспорта'))
    visa_passport_end = models.DateField(_('Date of expiry/Дата окончания'))
    visa_passport_city = models.CharField(_('Country of issue/Страна выдачи'),
                                        max_length=100)

    visa_hotel_address = models.CharField(_('Address of hotel lodging in Cyprus/Адрес гостиницы размещения на кипре'),
                                        max_length=150)

    def __str__(self):
        return self.visa_full_name_cyrillic
    class Meta:
        verbose_name_plural = 'Визы'
        verbose_name = 'Виза'
