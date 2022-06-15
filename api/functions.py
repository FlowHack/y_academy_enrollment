from django.db.models import QuerySet, Sum

from mega_market.models import ShopUnit

from .exceptions import EmptyValue


def if_none_400(value):
    if value is None or value == '':
        raise EmptyValue('Validation Failed')
    return value


def get_summ_count_price_category(unit: QuerySet, summ=0, count=0):
    childrens = unit.shop_units.all()

    categories = childrens.filter(type=ShopUnit.TypeUnit.CATEGORY)
    offers = childrens.filter(type=ShopUnit.TypeUnit.OFFER)
    result_summ = offers.aggregate(Sum('price'))['price__sum']
    summ += 0 if result_summ is None else result_summ
    count += offers.count()

    summ_childrens, count_childrens = get_summ_and_count(categories, summ, count)
    summ += summ_childrens
    count += count_childrens

    return summ, count


def get_summ_and_count(childrens, summ, count):
    for item in childrens:
        summ_item, count_item = get_summ_count_price_category(item)
        summ += summ_item
        count += count_item

    return summ, count
