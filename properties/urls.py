from django.urls import path # type: ignore
from .views import property_list

urlpatterns = [
    path('properties/', property_list, name='property_list'),
]
