
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from .views import  signup, Profile, ProfileDetailView, ProfileUpdate, UserList, ProfileDetail, user_profile






app_name ="accounts"
urlpatterns = [

	path('users/', UserList.as_view(template_name= "user_list.html", ), name= "user_list"),
    path('login/', LoginView.as_view(template_name= "login.html",  ), name= "login"),
    path('logout/', LogoutView.as_view(template_name = 'logout.html'),name= "logout"),
    path('register/', signup, name ="register"),
    path('<int:pk>', ProfileDetail.as_view(), name = 'profile'),
    path('<nickname>/update/', ProfileUpdate.as_view(), name = 'update'),
    # path('<nickname>',user_profile, name = 'detail'),
    # path('messages/',include(django_messages_urls), name = 'messages')


    
]