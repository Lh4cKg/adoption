from django.urls import path
from .views import Index, Home

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('home/', Home.as_view(), name="home"),
]
