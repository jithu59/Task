from django.contrib import admin

from .models import District, Region, Field
from . models import City

admin.site.register(District)
admin.site.register(City)
admin.site.register(Region)
admin.site.register(Field)