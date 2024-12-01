import pytest
from django.urls import reverse
from service.models import DishType, Cook, Dish
from decimal import Decimal


@pytest.mark.django_db
def test_index_view(client, django_user_model):
    user = django_user_model.objects.create_user(username="testuser", password="password")
    client.login(username="testuser", password="password")

    response = client.get(reverse("restaurant_kitchen:index"))
    assert response.status_code == 200
    assert "num_cooks" in response.context
    assert "num_dishes" in response.context
    assert "num_dish_types" in response.context
    assert "num_visits" in response.context


@pytest.mark.django_db
def test_dish_type_list_view(client, logged_in_user):
    response = client.get(reverse("restaurant_kitchen:dish_type_list"))
    assert response.status_code == 200
    assert "dish_types" in response.context


@pytest.mark.django_db
def test_dish_type_create_view(client, logged_in_user):
    response = client.post(reverse("restaurant_kitchen:dish_type_create"), {"name": "Sushi"})
    assert response.status_code == 302  # Redirects to dish_type_list after creation
    assert DishType.objects.filter(name="Sushi").exists()


@pytest.mark.django_db
def test_cook_list_view(client, logged_in_user):
    response = client.get(reverse("restaurant_kitchen:cook_list"))
    assert response.status_code == 200
    assert "cooks" in response.context


@pytest.mark.django_db
def test_cook_create_view(client, logged_in_user):
    response = client.post(reverse("restaurant_kitchen:cook_create"), {
        "username": "chef2",
        "first_name": "Test",
        "last_name": "Cook",
        "years_of_experience": 5
    })
    assert response.status_code == 302  # Redirects to cook_list after creation
    assert Cook.objects.filter(username="chef2").exists()


@pytest.mark.django_db
def test_dish_list_view(client, logged_in_user):
    response = client.get(reverse("restaurant_kitchen:dish_list"))
    assert response.status_code == 200
    assert "dishes" in response.context


@pytest.mark.django_db
def test_dish_create_view(client, logged_in_user):
    dish_type = DishType.objects.create(name="Sushi")
    cook = Cook.objects.create(username="chef2")

    response = client.post(reverse("restaurant_kitchen:dish_create"), {
        "name": "California Roll",
        "price": "8.50",
        "dish_type": dish_type.id,
        "cooks": cook.id,
        "description": "Popular sushi roll with avocado and crab"
    })
    assert response.status_code == 302  # Redirects to dish_list after creation
    assert Dish.objects.filter(name="California Roll").exists()


@pytest.mark.django_db
def test_dish_type_update_view(client, logged_in_user):
    dish_type = DishType.objects.create(name="Sushi")
    response = client.post(
        reverse("restaurant_kitchen:dish_type_update", args=[dish_type.id]),
        {"name": "Updated Sushi"}
    )
    assert response.status_code == 302  # Redirects to dish_type_list after update
    dish_type.refresh_from_db()
    assert dish_type.name == "Updated Sushi"


@pytest.mark.django_db
def test_dish_type_delete_view(client, logged_in_user):
    dish_type = DishType.objects.create(name="Sushi")
    response = client.post(reverse("restaurant_kitchen:dish_type_delete", args=[dish_type.id]))
    assert response.status_code == 302  # Redirects to dish_type_list after delete
    assert not DishType.objects.filter(id=dish_type.id).exists()


@pytest.mark.django_db
def test_cook_update_view(client, logged_in_user):
    cook = Cook.objects.create(username="chef1", first_name="Gordon", last_name="Ramsay")
    response = client.post(
        reverse("restaurant_kitchen:cook_update", args=[cook.id]),
        {"username": "chef1", "first_name": "Updated", "last_name": "Ramsay", "years_of_experience": 10}
    )
    assert response.status_code == 302  # Redirects to cook_list after update
    cook.refresh_from_db()
    assert cook.first_name == "Updated"
    assert cook.years_of_experience == 10


@pytest.mark.django_db
def test_cook_delete_view(client, logged_in_user):
    cook = Cook.objects.create(username="chef1")
    response = client.post(reverse("restaurant_kitchen:cook_delete", args=[cook.id]))
    assert response.status_code == 302  # Redirects to cook_list after delete
    assert not Cook.objects.filter(id=cook.id).exists()


@pytest.mark.django_db
def test_dish_update_view(client, logged_in_user):
    dish_type = DishType.objects.create(name="Sushi")
    cook = Cook.objects.create(username="chef2")
    dish = Dish.objects.create(
        name="California Roll",
        description="Popular sushi roll",
        price=8.50,
        dish_type=dish_type,
        cooks=cook
    )
    response = client.post(
        reverse("restaurant_kitchen:dish_update", args=[dish.id]),
        {
            "name": "Updated Roll",
            "description": "Updated description",
            "price": Decimal("9.99"),
            "dish_type": dish_type.id,
            "cooks": cook.id
        }
    )
    assert response.status_code == 302  # Redirects to dish_list after update
    dish.refresh_from_db()
    assert dish.name == "Updated Roll"
    assert dish.description == "Updated description"
    assert dish.price == Decimal("9.99")


@pytest.mark.django_db
def test_dish_delete_view(client, logged_in_user):
    dish_type = DishType.objects.create(name="Sushi")
    cook = Cook.objects.create(username="chef2")
    dish = Dish.objects.create(
        name="California Roll",
        description="Popular sushi roll",
        price=8.50,
        dish_type=dish_type,
        cooks=cook
    )
    response = client.post(reverse("restaurant_kitchen:dish_delete", args=[dish.id]))
    assert response.status_code == 302  # Redirects to dish_list after delete
    assert not Dish.objects.filter(id=dish.id).exists()
