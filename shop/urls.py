from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from product.views import IndexPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('products/', include('product.urls')),
    path('', IndexPageView.as_view(), name="index"),
    path('cart/', include('order.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)