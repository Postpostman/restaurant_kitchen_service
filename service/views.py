from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from .models import Cook, Dish, DishType


@login_required
def index(request):
    """Home page view function."""

    num_cooks = Cook.objects.count()
    num_dishes = Dish.objects.count()
    num_dishes_types = DishType.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_cooks" : num_cooks,
        "num_dishes" : num_dishes,
        "num_dishes_types" : num_dishes_types,
        "num_visits" : num_visits + 1,
        "ASSETS_ROOT" : settings.ASSETS_ROOT
    }

    return render(request)