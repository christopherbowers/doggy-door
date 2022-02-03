from asyncore import read
from dataclasses import fields
from rest_framework import serializers
from .models import Dog, Breed, Shelter

class DogSerializer(serializers.HyperlinkedModelSerializer):
    breed = serializers.HyperlinkedRelatedField(
        view_name='breed_detail',
        many=True,
        read_only=True
    )

    breed_url = serializers.ModelSerializer.serializer_url_field(
        view_name='breed_detail'
    )

    class Meta:
        model = Dog
        fields = ('id', 'dog_id', 'name', 'age', 'breed', 'color', 'description', 'adopted', 'likes')


class BreedSerializer(serializers.HyperlinkedModelSerializer):
    dog = serializers.HyperlinkedRelatedField(
        view_name='dog_detail',
        read_only=True
    )

    dog_id = serializers.PrimaryKeyRelatedField(
        queryset=Dog.objects.all(),
        source='dog'
    )

    class Meta:
        model = Breed
        fields = ('id', 'dog', 'dog_id', 'name')


class ShelterSerializer(serializers.HyperlinkedModelSerializer):
    dog = serializers.HyperlinkedRelatedField(
        view_name='dog_detail',
        read_only=True
    )

    dog_id = serializers.PrimaryKeyRelatedField(
        queryset=Dog.objects.all(),
        source='dog'
    )

    class Meta:
        model = Shelter
        fields = ('id', 'dog', 'dog_id', 'name')
