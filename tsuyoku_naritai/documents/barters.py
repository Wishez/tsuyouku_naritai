# -*- encoding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from people.models import Partners, Contractors, Employers, Artists

class Barters(models.Model):
    barter_number = models.CharField(_('Порядковый номер'),
                                    max_length=300)

    barter_artist = models.ForeignKey(
        Artists,
        _('Артист'),
        blank=True,
        null=True)
    barter_partner = models.ForeignKey(
        Partners,
        _('Партнёр'),
        blank=True,
        null=True)
    barter_contractor = models.ForeignKey(
        Contractors,
        _('Подрядчик'),
        blank=True,
        null=True)

    barter_manager = models.ForeignKey(
        Employers,
        _('Мэнеджер'),
        blank=True,
        null=True)

    def __str__(self):
        return self.barters_number
    class Meta:
        verbose_name_plural = 'Бартер'
        verbose_name = 'Бартер'