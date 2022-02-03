from rest_framework import generics
from .serializers import ArtistSerializer, SongSerializer
from .models import Dog, Shelter, Breeds

# Create your views here.
#  dog views
class DogList(generics.ListCreateAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

class DogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

#  shelter views
class ShelterList(generics.ListCreateAPIView):
    queryset = Shelter.objects.all()
    serializer_class = ShelterSerializer

class ShelterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shelter.objects.all()
    serializer_class = ShelterSerializer

#  breed views
class BreedList(generics.ListCreateAPIView):
    queryset = Breeds.objects.all()
    serializer_class = BreedSerializer

class BreedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Breeds.objects.all()
    serializer_class = BreedSerializer