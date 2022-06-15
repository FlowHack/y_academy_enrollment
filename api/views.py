import re

from django.utils import dateparse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from mega_market.models import ShopUnit

from .functions import EmptyValue, if_none_400
from .serializers import UnitSerialize


@api_view(['POST'])
def import_units(request):
    if request.method == 'POST':
        pattern = re.compile(
            r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'
        )

        try:
            date = dateparse.parse_datetime(request.data.get('updateDate'))
            items = if_none_400(request.data.get('items'))

            for item in items:
                id = if_none_400(item.get('id'))

                parent_id = item.get('parentId')
                if not pattern.match(id):
                    raise ValueError('Validation Failed')
                if parent_id not in [None, '']:
                    if not pattern.match(parent_id):
                        raise ValueError('Validation Failed')

                name = if_none_400(item.get('name'))
                offer = ShopUnit.TypeUnit.OFFER
                category = ShopUnit.TypeUnit.CATEGORY
                type = if_none_400(item.get('type'))

                type = (offer, category)[type == 'CATEGORY']
                price = 0 if type == category else  \
                    if_none_400(item.get('price'))

                unit = ShopUnit(
                    id=if_none_400(item.get('id')), name=name,
                    type=type, price=price, date=date
                )
                if parent_id is not None:
                    parent_unit = ShopUnit.objects.get(id=parent_id)
                    unit.parentId = parent_unit
                    while parent_unit is not None:
                        parent_unit.date = date
                        parent_unit.save()
                        parent_unit = parent_unit.parentId
                unit.save()

            return Response(status=status.HTTP_200_OK)

        except (EmptyValue, ValueError, ShopUnit.DoesNotExist) as e:
            print(str(e))
            return Response(
                {'message': 'Validation Failed'},
                status=status.HTTP_400_BAD_REQUEST
            )


@api_view(['GET', 'DELETE'])
def get_delete_unit(request, id_unit):
    try:
        unit = ShopUnit.objects.get(id=id_unit)
    except ShopUnit.DoesNotExist:
        return Response(
            {'message': 'Item not found'}, status=status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        return Response(UnitSerialize(unit).data, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        unit.delete()
        return Response(status=status.HTTP_200_OK)
