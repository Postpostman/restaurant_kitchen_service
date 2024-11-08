from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class DishType(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Dish_type'
        verbose_name_plural = 'Dishes_types'


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(null=True, blank=True, default=0)


    groups = models.ManyToManyField(
        Group,
        related_name="cook_user_set",
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups"
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="cook_user_permissions_set",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"


class Dish(models.Model):
    name = models.CharField(max_length=63)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE, related_name="dishes")
    cooks = models.ForeignKey(Cook, related_name="dishes", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Dish'
        verbose_name_plural = 'Dishes'
