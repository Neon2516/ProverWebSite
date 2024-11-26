from django.contrib import admin
from .models import Cars  # Импортируйте вашу модель

class CarsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Cars, CarsAdmin)
