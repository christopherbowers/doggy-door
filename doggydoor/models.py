from django.db import models

# Create your models here.
class Breeds(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name


class Dog(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.ForeignKey(Breeds, on_delete=models.CASCADE, related_name='dogs')
    color = models.CharField(max_length=100)
    description = models.TextField(max_length=225)
    adopted = models.BooleanField()
    likes = models.TextField(max_length=225)
    image = models.TextField(max_length=225)
    
    def __str__(self):
        return self.name




class Shelter(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE, related_name='shelters')

    def __str__(self):
        return self.name