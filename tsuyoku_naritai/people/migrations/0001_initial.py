# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 11:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('documents', '0001_initial'),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artists',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_name', models.CharField(max_length=200, verbose_name='Название группы/Имя артиста')),
                ('artist_site', models.URLField(default='https://', max_length=300, verbose_name='Сайт площадки')),
                ('artist_instagram', models.URLField(default='https://www.instagram.com/', max_length=300, verbose_name='Инстаграм')),
                ('artist_from_recommendation', models.CharField(default=None, max_length=150, null=True, verbose_name='По рекомендации')),
                ('artist_from_internet', models.CharField(default=None, max_length=150, null=True, verbose_name='Из интернета')),
                ('artist_from_event', models.CharField(default=None, max_length=150, null=True, verbose_name='С мероприятия')),
                ('artist_cooperated', models.NullBooleanField(default=False, verbose_name='Работали с ним или нет')),
                ('artist_is_in_moscow', models.BooleanField(default=False, verbose_name='Москва')),
                ('artist_in_moscow_region', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Московская область')),
                ('artist_in_regions', models.CharField(blank=True, default=None, max_length=150, null=True, verbose_name='Регионы')),
                ('artist_region', models.CharField(blank=True, max_length=100, null=True, verbose_name='Область')),
                ('artist_city', models.CharField(max_length=100, verbose_name='Город')),
                ('artist_locality', models.CharField(blank=True, max_length=150, null=True, verbose_name='Населённый пункт')),
                ('artist_street', models.CharField(max_length=150, verbose_name='Улица')),
                ('artist_house_num', models.DecimalField(decimal_places=0, default=0, max_digits=500, verbose_name='Дом')),
                ('artist_house_case', models.CharField(max_length=8, verbose_name='Корпус')),
                ('artist_house_entrance', models.DecimalField(decimal_places=0, default=0, max_digits=1000, verbose_name='Подъезд')),
                ('artist_floor', models.DecimalField(decimal_places=0, default=0, max_digits=100, verbose_name='Этаж')),
                ('artist_office', models.CharField(max_length=150, verbose_name='Офис')),
                ('artist_address_note', models.TextField(max_length=450, verbose_name='Примечание')),
                ('artist_prepayment', models.CharField(max_length=50, verbose_name='Предоплата')),
                ('artist_prepayment_order', models.TextField(max_length=100, verbose_name='Порядок предоплаты')),
                ('artist_agency_payment', models.IntegerField(default=0, verbose_name='Агентские %')),
                ('artist_contact_person', models.CharField(max_length=150, verbose_name='Имя контактного лица')),
                ('artist_contact_person_phone', phonenumber_field.modelfields.PhoneNumberField(default='+7', max_length=24, verbose_name='Телефон контактного лица')),
                ('artist_contact_person_email', models.EmailField(max_length=120, verbose_name='Электронная почта')),
                ('artist_stage_negotiations_date', models.DateField(default=django.utils.timezone.now, verbose_name='Дата')),
                ('artist_agreement', models.TextField(max_length=400, verbose_name='Результат договорённости')),
                ('artist_date_meeting', models.DateTimeField(verbose_name='Дата и время следующего контакта/Встречи')),
                ('artist_stage_negotiations_note', models.TextField(max_length=400, verbose_name='Примечание')),
                ('artist_date_performance', models.DateTimeField(verbose_name='Дата и время выступления')),
            ],
            options={
                'verbose_name': 'Артист',
                'verbose_name_plural': 'Артисты',
            },
        ),
        migrations.CreateModel(
            name='Contractors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contractor_title', models.CharField(max_length=100, verbose_name='Название')),
                ('contractor_type', models.CharField(choices=[('Техническое соправождение', 'Техническое соправождение(Свет/Звук)'), ('Оборудование/Декорации', 'Оборудование - Декорации'), ('Кейтринг', 'Кейтринг'), ('Транспорт', 'Транспорт(Авто)'), ('Декор/Оформление/Цветы', 'Декор - Оформление - Цветы'), ('Монтаж', 'Монтаж (Фото/Видео)'), ('Торты/Сладкое', 'Торты - Сладкое'), ('Полиграфия/Сувенирка', 'Полиграфия - Сувенирка'), ('Наемный персонал', 'Наемный персонал'), ('Стилисты/Визажисты', 'Стилисты - Визажисты')], default='TCHHD', max_length=50, verbose_name='Тип Подрядчика')),
                ('service_worker_type', models.CharField(blank=True, choices=[('Клининговые службы', 'Клининговые службы'), ('Грузчики', 'Грузчики'), ('Промышленные альпинисты', 'Промышленные альпинисты'), ('Промо-персонал', 'Промо-персонал'), ('Монтажники', 'Монтажники'), ('Организация парковки', 'Организация парковки / парковщики'), ('Хостес', 'Модели на мерпориятие / Хостес'), ('Охрана', 'Охрана'), ('Официанты', 'Официанты'), ('Бармены', 'Бармены')], default=None, max_length=50, null=True, verbose_name='Тип наёмного персонала')),
                ('contractor_nearest_underground', models.CharField(max_length=100, verbose_name='Ближайшее метро')),
                ('contractor_site', models.URLField(default='https://', max_length=150, verbose_name='Сайт')),
                ('contractor_instagram', models.URLField(default='https://www.instagram.com/', max_length=150, verbose_name='Инстаграм')),
                ('contractor_from_recommendation', models.BooleanField(default=False, verbose_name='Пришёл по рекомендации')),
                ('contractor_from_internet', models.BooleanField(default=False, verbose_name='Пришёл через интернет')),
                ('contractor_from_event', models.CharField(blank=True, max_length=150, null=True, verbose_name='Пришёл с мероприятия')),
                ('contractor_cooperated', models.NullBooleanField(default=False, verbose_name='Работали прежде или нет')),
                ('contractor_is_moscow', models.BooleanField(default=False, verbose_name='Москва')),
                ('contractor_moscow_region', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Московская область')),
                ('contractor_regions', models.CharField(blank=True, default=None, max_length=150, null=True, verbose_name='Регионы')),
                ('contractor_payment', models.IntegerField(default=0, verbose_name='Стоимость')),
                ('contractor_service', models.TextField(max_length=1000, verbose_name='Что входит в стоимость')),
                ('contractor_additional_service', models.CharField(blank=True, max_length=350, null=True, verbose_name='Дополнительные услуги')),
                ('contractor_prepayment', models.CharField(max_length=12, verbose_name='Предоплата')),
                ('contractor_agency_payment', models.CharField(default=0, max_length=150, null=True, verbose_name='Агенские %')),
                ('contractor_contact_person', models.CharField(max_length=150, verbose_name='Имя контактного лица')),
                ('contractor_contact_person_phone', phonenumber_field.modelfields.PhoneNumberField(default='+7', max_length=24, verbose_name='Телефон контактного лица')),
                ('contractor_contact_note', models.TextField(max_length=450, verbose_name='Примечание')),
                ('contractor_region', models.CharField(blank=True, max_length=100, null=True, verbose_name='Область')),
                ('contractor_city', models.CharField(max_length=100, verbose_name='Город')),
                ('contractor_locality', models.CharField(blank=True, max_length=150, null=True, verbose_name='Населённый пункт')),
                ('contractor_street', models.CharField(max_length=150, verbose_name='Улица')),
                ('contractor_house_num', models.DecimalField(decimal_places=0, default=0, max_digits=500, verbose_name='Дом')),
                ('contractor_house_case', models.CharField(default='2A', max_length=8, verbose_name='Корпус')),
                ('contractor_house_entrance', models.DecimalField(decimal_places=0, default=0, max_digits=1000, verbose_name='Подъезд')),
                ('contractor_floor', models.DecimalField(decimal_places=0, default=0, max_digits=100, verbose_name='Этаж')),
                ('contractor_office', models.CharField(max_length=150, verbose_name='Офис')),
                ('contractor_address_note', models.TextField(max_length=450, verbose_name='Примечание')),
            ],
            options={
                'verbose_name': 'Подрядчик',
                'verbose_name_plural': 'Подрядчики',
            },
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_full_name', models.CharField(max_length=300, verbose_name='ФИО')),
                ('customer_phone', phonenumber_field.modelfields.PhoneNumberField(default='+7', max_length=24, verbose_name='Телефон')),
                ('customer_email', models.EmailField(max_length=150, verbose_name='E-mail')),
                ('customer_account', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Аккаунт клиента')),
                ('customer_visa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='documents.Visa', verbose_name='Виза клиента')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Employers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employer_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='Порядковый номер')),
                ('employer_first_name', models.CharField(max_length=200, verbose_name='Имя')),
                ('employer_last_name', models.CharField(max_length=200, verbose_name='Фамилия')),
                ('employer_date_birthday', models.DateField(verbose_name='Дата рождения')),
                ('employer_avatar', models.FileField(upload_to='employer_avatars/', verbose_name='Фото')),
                ('employer_post', models.CharField(max_length=200, verbose_name='Должность')),
                ('employer_city', models.CharField(max_length=200, verbose_name='Город')),
                ('employer_account', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Аккаунт сотрудника')),
                ('employer_visa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='documents.Visa', verbose_name='Виза сотрудника')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner_name', models.CharField(max_length=150, verbose_name='Имя')),
                ('partner_phone', phonenumber_field.modelfields.PhoneNumberField(default='+7', max_length=24, verbose_name='Телефон')),
                ('partner_email', models.EmailField(max_length=100, verbose_name='Email')),
                ('partner_site', models.URLField(verbose_name='Сайт')),
                ('partner_note', models.TextField(blank=True, max_length=300, null=True, verbose_name='Примечание')),
            ],
            options={
                'verbose_name': 'Партнёр',
                'verbose_name_plural': 'Партнёры',
            },
        ),
        migrations.AddField(
            model_name='artists',
            name='artist_manager_name',
            field=models.ManyToManyField(to='people.Employers', verbose_name='Имя Менеджера'),
        ),
        migrations.AddField(
            model_name='artists',
            name='artist_type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.ArtistTypes', verbose_name='Тип артиста'),
        ),
    ]