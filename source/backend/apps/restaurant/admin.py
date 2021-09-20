from django.contrib import admin

from .models import Restaurant

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ("id", "rating", "name", "site", "email", "phone", "street", "city", "state", "lat", "lng")
    search_fields = ["id", "rating", "name", "site", "email", "phone", "street", "city", "state", "lat", "lng"]
    fields = ("id", "rating", "name", "site", "email", "phone", "street", "city", "state", "lat", "lng")

admin.site.register(Restaurant)