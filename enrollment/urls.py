from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
<<<<<<< HEAD
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'redoc/', TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
    path('', include('mega_market.urls', namespace='mega_market')),
    path('', include('api.urls', namespace='api')),
=======
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mega_market.urls', namespace='mega_market'))
>>>>>>> aa5c1e7f8a54dd75a843e262474e3c768579e401
]


urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
urlpatterns += static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
)
