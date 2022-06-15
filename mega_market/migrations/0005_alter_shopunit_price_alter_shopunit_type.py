# Generated by Django 4.0.5 on 2022-06-15 14:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mega_market', '0004_remove_shopunit_children'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopunit',
            name='price',
            field=models.IntegerField(blank=True, default=0, help_text='Укажите цену товара', null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Цена товара'),
        ),
        migrations.AlterField(
            model_name='shopunit',
            name='type',
            field=models.TextField(choices=[('OFFER', 'Продукт'), ('CATEGORY', 'Категория')], help_text='Выберите тип объекта', verbose_name='Тип объекта (Категория/Товар)'),
        ),
    ]