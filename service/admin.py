from django.contrib import admin
from .models import DishType, Cook, Dish


# Registering DishType model
@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)



# Registering Cook model
@admin.register(Cook)
class CookAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'years_of_experience')
    search_fields = ('username', 'first_name', 'last_name')
    list_filter = ('years_of_experience',)


# Registering Dish model
@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'dish_type', 'cooks')
    search_fields = ('name', 'description')
    list_filter = ('dish_type', 'cooks')
