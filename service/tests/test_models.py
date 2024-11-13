import pytest
from service.models import DishType, Cook, Dish

@pytest.mark.django_db
def test_dish_type_str():
    dish_type = DishType.objects.create(name="Sushi")
    assert str(dish_type) == "Sushi"

@pytest.mark.django_db
def test_cook_str():
    cook = Cook.objects.create(username="chef1", first_name="Gordon", last_name="Ramsay")
    assert str(cook) == "Gordon Ramsay (chef1)"

@pytest.mark.django_db
def test_dish_str():
    dish_type = DishType.objects.create(name="Pasta")
    cook = Cook.objects.create(username="chef2")
    dish = Dish.objects.create(
        name="Spaghetti",
        description="Delicious Italian pasta",
        price=12.50,
        dish_type=dish_type,
        cooks=cook
    )
    assert str(dish) == "Spaghetti"

