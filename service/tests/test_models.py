from django.test import TestCase
from service.models import DishType, Cook, Dish
from django.contrib.auth.models import User


class DishTypeModelTest(TestCase):
    def setUp(self):
        self.dish_type = DishType.objects.create(name="Appetizer")

    def test_dish_type_str(self):
        self.assertEqual(str(self.dish_type), "Appetizer")


class CookModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="chef", password="password")
        self.cook = Cook.objects.create(user=self.user, years_of_experience=5)

    def test_cook_str(self):
        self.assertEqual(str(self.cook), "chef chef (chef)")


class DishModelTest(TestCase):
    def setUp(self):
        self.dish_type = DishType.objects.create(name="Main Course")
        self.cook = Cook.objects.create(username="chef", first_name="Chef", last_name="Cook")
        self.dish = Dish.objects.create(
            name="Pasta",
            description="Delicious pasta",
            price=12.99,
            dish_type=self.dish_type,
            cooks=self.cook
        )

    def test_dish_str(self):
        self.assertEqual(str(self.dish), "Taco")
