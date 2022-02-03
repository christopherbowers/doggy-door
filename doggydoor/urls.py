from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('dogs/', views.DogList.as_view(), name='dog_list'),
    path('dogs/<int:pk>', views.DogDetail.as_view(), name='dog_detail'),
    path('shelters/', views.ShelterList.as_view(), name='shelter_list'),
    path('shelters/<int:pk>', views.ShelterDetails.as_view(), name='shelter_details'),
    path('breeds/', views.BreedList.as_view(), name='breed_list'),
    path('breeds/<int:pk>', views.BreedDetails.as_view(), name='breed_details')
]