from .views import AnimalCreateView,  AnimalListView, animals_listview, AnimalDetailView
from django.urls import path, include
from django.urls import reverse



app_name= "animals"


urlpatterns = [
    # path('animals/<slug>', AnimalListView.as_view(), name= "list" ),
    path('create/', AnimalCreateView.as_view(model = "Animal",success_url="/animals/list/"), name= "create"),
    path('list/', animals_listview),
    path('/<int:pk>/', AnimalDetailView.as_view()),
    ]
