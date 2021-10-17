from django.contrib import admin
from . models import joinus, researchpaper, alumini

# Register your models here.

admin.site.register(researchpaper)
admin.site.register(joinus)
admin.site.register(alumini)