from datetime import datetime

from rest_framework import serializers

from api.functions import get_summ_count_price_category
from mega_market.models import ShopUnit


class UnitSerialize(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ShopUnit

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['date'] = instance.date.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'

        if instance.type == ShopUnit.TypeUnit.CATEGORY:
            childrens = instance.shop_units.all()
            if childrens.count() == 0:
                rep['children'] = None
                return rep
            summ, count = get_summ_count_price_category(instance)
            rep['price'] = 0 if count == 0 else round(summ / count)
            rep['children'] = [UnitSerialize(item).data for item in childrens]
            return rep

        rep['children'] = None
        return rep
