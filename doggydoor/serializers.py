# from asyncore import read
# from dataclasses import fields
from rest_framework import serializers
from .models import Dog, Breed, Shelter

class DogSerializer(serializers.HyperlinkedModelSerializer):
    breed = serializers.HyperlinkedRelatedField(
        view_name='breed_detail',
        read_only=True
    )

    breed_id = serializers.PrimaryKeyRelatedField(
        queryset=Breed.objects.all(),
        source='breed'
    )

    shelter = serializers.HyperlinkedRelatedField(
        view_name='shelter_detail',
        read_only=True
    )
    

    dog_url = serializers.ModelSerializer.serializer_url_field(
        view_name='dog_detail'
    )

    class Meta:
        model = Dog
        fields = ('id', 'name', 'age', 'breed', 'color', 'description', 'adopted', 'likes', 'dog_url', 'breed_id', 'shelter', 'image')


class BreedSerializer(serializers.HyperlinkedModelSerializer):
    dogs = serializers.HyperlinkedRelatedField(
        view_name='dog_detail',
        many=True,
        read_only=True
    )

    breed_url = serializers.ModelSerializer.serializer_url_field(
        view_name='breed_detail'
    )

    class Meta:
        model = Breed
        fields = ('id', 'dogs', 'breed_url', 'name')



class ShelterSerializer(serializers.HyperlinkedModelSerializer):
    shelters = serializers.HyperlinkedRelatedField(
        view_name='dog_detail',
        many=True,
        read_only=True
    )

    shelter_url = serializers.ModelSerializer.serializer_url_field(
        view_name='shelter_detail'
    )

    class Meta:
        model = Shelter
        fields = ('id', 'name', 'location', 'shelter_url', 'shelters')

