from django.urls import path
from django.contrib import admin
from service.views import(
    index,
    CookListView,
    CookDetailView,
    CookCreateView,
    CookUpdateView,
    CookDeleteView,
    DishTypeListView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    DishTypeDetailView,
    DishListView,
    DishDetailView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
)

app_name = "restaurant_kitchen"

urlpatterns = [
    path("", index, name="index"),
    # DishType URLs
    path('dish_types/', DishTypeListView.as_view(), name='dish_type_list'),
    path('dish_types/<int:pk>/', DishTypeDetailView.as_view(), name='dish_type_detail'),
    path('dish_types/create/', DishTypeCreateView.as_view(), name='dish_type_create'),
    path('dish_types/<int:pk>/update/', DishTypeUpdateView.as_view(), name='dish_type_update'),
    path('dish_types/<int:pk>/delete/', DishTypeDeleteView.as_view(), name='dish_type_delete'),

    # Cook URLs
    path('cooks/', CookListView.as_view(), name='cook_list'),
    path('cooks/<int:pk>/', CookDetailView.as_view(), name='cook_detail'),
    path('cooks/create/', CookCreateView.as_view(), name='cook_create'),
    path('cooks/<int:pk>/update/', CookUpdateView.as_view(), name='cook_update'),
    path('cooks/<int:pk>/delete/', CookDeleteView.as_view(), name='cook_delete'),

    # Dish URLs
    path('dishes/', DishListView.as_view(), name='dish_list'),
    path('dishes/<int:pk>/', DishDetailView.as_view(), name='dish_detail'),
    path('dishes/create/', DishCreateView.as_view(), name='dish_create'),
    path('dishes/<int:pk>/update/', DishUpdateView.as_view(), name='dish_update'),
    path('dishes/<int:pk>/delete/', DishDeleteView.as_view(), name='dish_delete'),
]
