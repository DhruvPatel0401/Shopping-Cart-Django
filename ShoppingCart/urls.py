from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("ShoppingCart.apps.productCatalogue.urls")),
    path("basket/", include("ShoppingCart.apps.basket.urls")),
    path("checkout/", include("ShoppingCart.apps.checkout.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
