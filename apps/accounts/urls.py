from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from .views import signup, Profile, ProfileDetailView, ProfileUpdate, UserList, ProfileDetail, user_profile

app_name = "accounts"
urlpatterns = [

<<<<<<< HEAD
    path('users/', UserList.as_view(template_name="accounts/user_list.html", ), name="user_list"),
    path('login/', LoginView.as_view(template_name="accounts/login.html", ), name="login"),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name="logout"),
    path('register/', signup, name="register"),
    # path('<nickname>', user_profile, name = 'profile'),
    path('<nickname>/update/', ProfileUpdate.as_view(), name='update'),
    path('<nickname>', user_profile, name='detail'),
=======
	path('users/', UserList.as_view(template_name= "user_list.html", ), name= "user_list"),
    path('login/', LoginView.as_view(template_name= "login.html",  ), name= "login"),
    path('logout/', LogoutView.as_view(template_name = 'logout.html'),name= "logout"),
    path('register/', signup, name ="register"),
    path('<int:pk>', ProfileDetail.as_view(), name = 'profile'),
    path('<nickname>/update/', ProfileUpdate.as_view(), name = 'update'),
    # path('<nickname>',user_profile, name = 'detail'),
>>>>>>> 7ee03d8301d5bb5a548113273c33f6bd5829feaf
    # path('messages/',include(django_messages_urls), name = 'messages')

]
