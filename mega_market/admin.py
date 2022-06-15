from django.contrib import admin
<<<<<<< HEAD

=======
>>>>>>> aa5c1e7f8a54dd75a843e262474e3c768579e401
from mega_market.models import ShopUnit


@admin.register(ShopUnit)
class ShopUnitAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ('id', 'type', 'name', 'date')
    search_filed = ('name',)
    list_filter = ('type', 'date')
=======
    list_display = ('type', 'name', 'type')
    search_filed = ('name',)
    list_filter = ('type',)
    exclude = ('date',)
>>>>>>> aa5c1e7f8a54dd75a843e262474e3c768579e401
    empty_value_display = '-пусто-'
