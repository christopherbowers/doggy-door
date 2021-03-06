# Generated by Django 4.0.2 on 2022-02-04 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Shelter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('color', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=225)),
                ('adopted', models.BooleanField()),
                ('likes', models.TextField(max_length=225)),
                ('image', models.TextField(max_length=225)),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dogs', to='doggydoor.breed')),
                ('shelter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shelters', to='doggydoor.shelter')),
            ],
        ),
    ]
