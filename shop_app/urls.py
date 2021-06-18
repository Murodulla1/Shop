from .views import shop

from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', shop, name="shop")
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)