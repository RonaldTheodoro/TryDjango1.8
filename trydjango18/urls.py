from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from newsletter.views import home, contact, login


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home),
    url(r'^form/', contact),
    url(r'^login/', login)
]

if settings.DEBUG:
    urlpatterns += static(
            settings.STATIC_URL,
            document_root=settings.STATIC_ROOT
    )
    urlpatterns += static(
            settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT
    )
