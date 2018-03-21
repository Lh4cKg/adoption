from .views import signup
from django.contrib.auth.views import LoginView
from django.urls import path, include







app_name ="accounts"
urlpatterns = [
 
    path('login/', LoginView.as_view(), name= "login"),
    path('register/', signup, name ="register"),
    
]