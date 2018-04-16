from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

app_name = "adoption"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("apps.home.urls")),
    path('animals/', include("apps.animals.urls")),
    path('accounts/', include("apps.accounts.urls")),
    path('messages/', include('apps.django_messages.urls')),
    # path('adopt/', include('requestadopt.urls')), # what is this?
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
