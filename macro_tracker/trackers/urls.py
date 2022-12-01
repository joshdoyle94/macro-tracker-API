from django.urls import path
from .views.list_views import ListsView, ListsDetailView
from .views.meal_views import MealsView, MealsDetailView


urlpatterns = [
    path('lists/', ListsView.as_view(), name='lists'),
    path('lists/<int:pk>/', ListsDetailView.as_view(), name='list'),
    path('meals/', MealsView.as_view(), name='meals'),
    path('meals/<int:pk>/', MealsDetailView.as_view(), name='meal'),
]