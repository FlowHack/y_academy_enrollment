from django.urls import path

from api import views

app_name = 'api'


urlpatterns = [
    path('imports', views.import_units, name='import_units'),
    path('delete/<str:id_unit>', views.get_delete_unit, name='delete_unit'),
    path('nodes/<str:id_unit>', views.get_delete_unit, name='get_unit')
]
