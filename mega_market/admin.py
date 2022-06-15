from django.contrib import admin
from mega_market.models import ShopUnit


@admin.register(ShopUnit)
class ShopUnitAdmin(admin.ModelAdmin):
    list_display = ('type', 'name', 'date')
    search_filed = ('name',)
    list_filter = ('type',)
    exclude = ('date',)
    empty_value_display = '-пусто-'
