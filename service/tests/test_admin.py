import pytest
from django.contrib.admin.sites import site
from service.models import DishType, Cook, Dish
from service.admin import DishTypeAdmin, CookAdmin, DishAdmin


@pytest.mark.django_db
def test_dish_type_admin_registration():
    assert DishType in site._registry
    assert isinstance(site._registry[DishType], DishTypeAdmin)
    assert site._registry[DishType].list_display == ('id', 'name')
    assert site._registry[DishType].search_fields == ('name',)


@pytest.mark.django_db
def test_cook_admin_registration():
    assert Cook in site._registry
    assert isinstance(site._registry[Cook], CookAdmin)
    assert site._registry[Cook].list_display == ('id', 'username', 'first_name', 'last_name', 'years_of_experience')
    assert site._registry[Cook].search_fields == ('username', 'first_name', 'last_name')
    assert site._registry[Cook].list_filter == ('years_of_experience',)


@pytest.mark.django_db
def test_dish_admin_registration():
    assert Dish in site._registry
    assert isinstance(site._registry[Dish], DishAdmin)
    assert site._registry[Dish].list_display == ('id', 'name', 'description', 'price', 'dish_type', 'cooks')
    assert site._registry[Dish].search_fields == ('name', 'description')
    assert site._registry[Dish].list_filter == ('dish_type', 'cooks')
