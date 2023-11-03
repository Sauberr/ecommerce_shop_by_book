from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from payment import webhooks


urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path(_('cart/'), include('cart.urls', namespace='cart')),
    path(_('orders/'), include('orders.urls', namespace='orders')),
    path(_('payment/'), include('payment.urls', namespace='payment')),
    path(_('coupons/'), include('coupons.urls', namespace='coupons')),
    path(_('rosetta/'), include('rosetta.urls')),
    path('', include('shop.urls', namespace='shop')),
)

urlpatterns += [
 path('payment/webhook/', webhooks.stripe_webhook,name='stripe-webhook'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)