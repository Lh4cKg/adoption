from django.urls import path
from .views import (AnimalCreateView, AnimalListView, AnimalDetailView, AnimalUpdateView, MyAnimalsListView,
                    AnimalDeleteView, add_comment_to_post)

app_name = "animals"

urlpatterns = [
    # path('animals/<slug>', AnimalListView.as_view(), name= "list" ),
    path('create/', AnimalCreateView.as_view(model="Animal", success_url="/animals/"), name="create"),
    path('mylist/', MyAnimalsListView.as_view(model="Animals"), name="list_animals"),
    path('<slug>/update/', AnimalUpdateView.as_view(model="Animals", success_url="/animals/mylist/"), name="update"),
    path('<slug>/delete/', AnimalDeleteView.as_view(), name="delete"),

    path('<slug>/', AnimalDetailView.as_view(), name="detail"),
    # path('myanimals/', MyAnimalsListView.as_view(model = "Animals"), name="mylist"),
    path('', AnimalListView.as_view(), name='list'),
    path('post/<slug>/comment/', add_comment_to_post, name='add_comment_to_post')
]
