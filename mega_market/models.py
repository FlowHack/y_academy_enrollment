import uuid
from django.db import models
import datetime
from django.core.validators import MinValueValidator


class ShopUnit(models.Model):
    class TypeUnit(models.TextChoices):
        OFFER = 'Продукт', 'OFFER'
        CATEGORY = 'Категория', 'CATEGORY'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        'Название объекта', max_length=100, null=False, blank=False,
        help_text='Введите название объекта'
    )
    date = models.DateTimeField(
        'Дата создания объекта/Дата изменения цены товара',
        default=datetime.datetime, null=False, blank=False
    )
    parent_id = models.ForeignKey(
        'self', null=False, blank=True, on_delete=models.CASCADE,
        verbose_name='id родительской категории', related_name='shop_units',
        help_text='Укажите категорию, к которой отнсится товар'
    )
    type = models.TextField(
        'Тип объекта (Категория/Товар)', choices=TypeUnit.choices,
        help_text='Выберите тип объекта', null=False, blank=False
    )
    price = models.IntegerField(
        'Цена товара', validators=[MinValueValidator(0)],
        help_text='Укажите цену товара', null=False, blank=True
    )

    class Meta:
        ordering = ('-date',)
        verbose_name = 'Объекты маркета'

    def __str__(self):
        text_representation = f'{self.type} - {self.name}'
        return text_representation if self.type == self.TypeUnit.CATEGORY  \
            else text_representation + f' - {self.price}'

    def parent(self):
        return self.shop_units.all()
