# -*- encoding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
# from django.utils.encoding import python_2_unicode_compatible
from mptt.models import MPTTModel, TreeForeignKey


class EventTypes(MPTTModel):

    type = models.CharField(_('Тип мероприятия'), max_length=150, unique=True)

    parent = TreeForeignKey('self',
                            null=True,
                            blank=True,
                            related_name='children',
                            db_index=True,
                            verbose_name=_('Родитесльский тип мероприятия'))

    def __str__(self):
        return self.type
    class Meta:
        verbose_name = 'Тип мероприятия'
        verbose_name_plural = 'Типы мероприятий'
    class MPTTMeta:
        order_insertion_by = ['type']
class ArtistTypes(models.Model):
    artist_type_name = models.CharField(_('Название типа артиста'),
                                        max_length=200)


    def __str__(self):
        return self.artist_type_name
    class Meta:
        verbose_name_plural = 'Типы артистов'
        verbose_name = 'Тип артиста'
class PlaceTypes(models.Model):
    place_type_name = models.CharField(_('Название типа площадки'),
                                       max_length=200)

    def __str__(self):
        return self.place_type_name

    class Meta:
        verbose_name = 'Тип площадки'
        verbose_name_plural = 'Типы площадок'

