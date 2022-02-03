# Generated by Django 4.0.2 on 2022-02-03 20:08

from django.db import migrations

def seed(apps, schema_editor):
    Breed = apps.get_model('doggydoor', 'Breed')
    Shelter = apps.get_model('doggydoor', 'Shelter')
    Dog = apps.get_model('doggydoor', 'Dog')
    




class Migration(migrations.Migration):

    dependencies = [
        ('doggydoor', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed, fallow)
    ]