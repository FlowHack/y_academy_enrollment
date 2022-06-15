# Generated by Django 4.0.5 on 2022-06-15 15:22

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mega_market', '0007_alter_shopunit_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopunit',
            name='date',
            field=models.DateTimeField(default=datetime.datetime, verbose_name='Дата создания объекта/Дата изменения цены товара'),
        ),
    ]
