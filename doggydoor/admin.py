from django.contrib import admin
from .models import Dog, Breeds, Shelter
# Register your models here.

admin.site.register(Dog)
admin.site.register(Breeds)
admin.site.register(Shelter)