import uuid

from datetime import datetime

from django.core.validators import MinValueValidator
from django.db import models


class ShopUnit(models.Model):
    class TypeUnit(models.TextChoices):
        OFFER = 'OFFER', 'Продукт'
        CATEGORY = 'CATEGORY', 'Категория'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        'Название объекта', max_length=100, null=False, blank=False,
        help_text='Введите название объекта'
    )
    date = models.DateTimeField(
        'Дата создания объекта/Дата изменения цены товара',
        default=datetime, null=False, blank=False
    )
    parentId = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.CASCADE,
        verbose_name='id родительской категории', related_name='shop_units',
        help_text='Укажите категорию, к которой отнсится товар'
    )
    type = models.TextField(
        'Тип объекта (Категория/Товар)', choices=TypeUnit.choices,
        help_text='Выберите тип объекта', null=False, blank=False
    )
    price = models.IntegerField(
        'Цена товара', validators=[MinValueValidator(0)],
        help_text='Укажите цену товара', null=True, blank=True,
        default=0
    )

    class Meta:
        ordering = ('-date',)
        verbose_name = 'Объекты маркета'

    def __str__(self):
        text_representation = f'{self.type} - {self.name}'
        return text_representation if self.type == self.TypeUnit.CATEGORY  \
            else text_representation + f' - {self.price}'
