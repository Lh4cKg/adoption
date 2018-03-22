from .views import signup
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include







app_name ="accounts"
urlpatterns = [
 
    path('login/', LoginView.as_view(template_name= "login.html"), name= "login"),
    path('logout/', LogoutView.as_view(template_name= "logout.html"),{'next_page': '/'}, name= "logout"),
    path('register/', signup, name ="register"),
    
]