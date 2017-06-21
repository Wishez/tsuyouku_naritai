from django.db import models
from django.utils.translation import ugettext_lazy as _
from people.models import Partners, Contractors, Employers, Artists

class Barters(models.Model):
    barter_number = models.CharField(_('Порядковый номер'),
                                     max_length=300)
    barter_date_start = models.DateField(_('Дата начала бартера'))
    barter_date_expiration = models.DateField(_('Дата окончания бартера'))

    barter_artist = models.ForeignKey(
        Artists,
        verbose_name=_('Артист'),
        blank=True,
        null=True)
    barter_partner = models.ForeignKey(
        Partners,
        verbose_name=_('Партнёр'),
        blank=True,
        null=True)
    barter_contractor = models.ForeignKey(
        Contractors,
        verbose_name=_('Подрядчик'),
        blank=True,
        null=True)

    barter_manager = models.ForeignKey(
        Employers,
        verbose_name=_('Мэнеджер'),
        blank=True,
        null=True)


    def __str__(self):
        return self.barters_number
    class Meta:
        verbose_name = 'Бартер'
        verbose_name_plural = 'Бартеры'

