# Generated by Django 4.0.2 on 2022-02-03 20:08

from django.db import migrations

def seed(apps, schema_editor):
    Breed = apps.get_model('doggydoor', 'Breed')
    Shelter = apps.get_model('doggydoor', 'Shelter')
    Dog = apps.get_model('doggydoor', 'Dog')
    # shelter info
    helping_paws_shelter = Shelter(name='Helping Paws Shelter', location='earth')
    cool_shelter = Shelter(name='Cool Shelter', location='moon')
    up_dog_shelter = Shelter(name='Up Dog Shelter', location='mars')
    down_dog_shelter = Shelter(name='Down Dog Shelter', location='up yours')
    fluffy_wuffy_shelter = Shelter(name='Fluffy Wuffy Shelter', location='guess where')
    helping_paws_shelter.save()
    cool_shelter.save()
    up_dog_shelter.save()
    down_dog_shelter.save()
    fluffy_wuffy_shelter.save()

    # dog breed info
    labradoodle = Breed(name='Labradoodle', description='it is a dog breed')
    a_dog_breed = Breed(name='A dog breed', description='it is a dog breed')
    husky = Breed(name='Husky', description='it is a dog breed')
    beegle = Breed(name='Beegle', description='it is a dog breed')
    pitt_bull = Breed(name='Pitt Bull', description='it is a dog breed')
    labradoodle.save()
    a_dog_breed.save()
    husky.save()
    beegle.save()
    pitt_bull.save()

    # dog info
    Dog(name = 'I dont need one', age = 30, shelter = cool_shelter, breed = a_dog_breed, color = 'ash', adopted = False, likes = 'nothing. this world is pain', description = 'this dog is too emo take him away', image = 'https://i.imgur.com/ig63VVR.png').save()
    Dog(name = 'Mr. Wiggles', age = 12, shelter = fluffy_wuffy_shelter, breed = pitt_bull, color = 'brown', adopted = False, likes = 'playing fetch', description = "he's a big ball of wagging", image = 'https://i.imgur.com/sdWEtoC.png').save()
    Dog(name = 'Drake', age = 8, shelter = helping_paws_shelter, breed = husky, color = 'gold', adopted = False, likes = "listening to God's Plan", description = 'he wants to be a rapper someday', image = 'https://i.imgur.com/pVppgqw.png').save()
    Dog(name = 'Billy-Bob', age = 6, shelter = down_dog_shelter, breed = labradoodle, color = 'rainbow', adopted = False, likes = 'enjoys greenery', description = 'this dog is too emo take him away', image = 'https://i.imgur.com/8mkt0zp.png').save()
    Dog(name = 'Dawg', age = 3, shelter = up_dog_shelter, breed = beegle, color = 'pink', adopted = False, likes = 'sleeping', description = 'from the streets', image = 'https://i.imgur.com/BBgC4K3.png').save()

def fallow(apps, schema_editor):
    Breed = apps.get_model('doggydoor', 'Breed')
    Dog = apps.get_model('doggydoor', 'Dog')
    Shelter = apps.get_model('doggydoor', 'Shelter')
    Breed.objects.all().delete()
    Dog.objects.all().delete()
    Shelter.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('doggydoor', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed, fallow)
    ]