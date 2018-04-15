from . import views, settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
from django.urls import path, include
from animals.views import AnimalCreateView
from animals.views import Index, Home
from django.conf import settings
from django.views.static import serve
from django.views.generic import TemplateView

app_name = "mysite"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(template_name = "index.html"), name = "index"),
    path('home/', Home.as_view(template_name="home.html"), name="home"),
    path('animals/', include("animals.urls")),
    path('accounts/',include("accounts.urls") ),
    path('messages/',include('django_messages.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
# 	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
