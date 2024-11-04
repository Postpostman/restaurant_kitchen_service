from django.urls import path
from django.contrib import admin
from service.views import(
    index
)

app_name = "restaurant_kitchen"

urlpatterns = [
    path("", index, name="index"),
    path("admin/", admin.site.urls),

