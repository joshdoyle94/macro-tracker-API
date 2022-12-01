from django.urls import path, include
from django.contrib import admin
from trackers.views.list_views import ListsViews
from trackers.views.meal_views import MealsViews
from rest_framework import routers


# urlpatterns = [
#     path('lists/', ListsView.as_view(), name='lists'),
#     path('lists/<int:pk>/', ListsDetailView.as_view(), name='list'),
#     path('meals/', MealsView.as_view(), name='meals'),
#     path('meals/<int:pk>/', MealsDetailView.as_view(), name='meal'),
# ]