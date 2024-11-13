from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponse
from .models import Cook, Dish, DishType
from django.urls import reverse_lazy
from django.views import generic
from django.db.models import Q



@login_required
def index(request):
    """Home page view function."""

    num_cooks = Cook.objects.count()
    num_dishes = Dish.objects.count()
    num_dish_types = DishType.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_cooks": num_cooks,
        "num_dishes": num_dishes,
        "num_dish_types": num_dish_types,
        "num_visits": num_visits + 1,
        "ASSETS_ROOT": settings.ASSETS_ROOT
    }

    return render(request, "index.html", context=context)


# Views for DishType
class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    template_name = "home/dish_type_list.html"
    context_object_name = "dish_types"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(name__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("q", "")
        return context



class DishTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = DishType
    template_name = "home/dish_type_detail.html"
    context_object_name = "dish_type"


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = ["name"]
    template_name = "home/dish_type_form.html"
    success_url = reverse_lazy("restaurant_kitchen:dish_type_list")


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = ["name"]
    template_name = "home/dish_type_form.html"
    success_url = reverse_lazy("restaurant_kitchen:dish_type_list")


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    template_name = "home/dish_type_confirm_delete.html"
    success_url = reverse_lazy("restaurant_kitchen:dish_type_list")


# Views for Cook
class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    template_name = "home/cook_list.html"
    context_object_name = "cooks"
    paginate_by = 10


    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(
                Q(first_name__icontains=query) | Q(last_name__icontains=query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("q", "")
        return context


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    template_name = "home/cook_detail.html"
    context_object_name = "cook"


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    fields = ["username", "first_name", "last_name", "years_of_experience"]
    template_name = "home/cook_form.html"
    success_url = reverse_lazy("restaurant_kitchen:cook_list")


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    fields = ["username", "first_name", "last_name", "years_of_experience"]
    template_name = "home/cook_form.html"
    success_url = reverse_lazy("restaurant_kitchen:cook_list")


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    template_name = "home/cook_confirm_delete.html"
    success_url = reverse_lazy("restaurant_kitchen:cook_list")


# Views for Dish
class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    template_name = "home/dish_list.html"
    context_object_name = "dishes"
    paginate_by = 10


    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) | Q(dish_type__name__icontains=query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("q", "")
        return context


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish
    template_name = "home/dish_detail.html"
    context_object_name = "dish"


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    fields = ["name", "price", "dish_type", "cooks", "description"]
    template_name = "home/dish_form.html"
    success_url = reverse_lazy("restaurant_kitchen:dish_list")


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    fields = ["name", "price", "dish_type", "cooks", "description"]
    template_name = "home/dish_form.html"
    success_url = reverse_lazy("restaurant_kitchen:dish_list")


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    template_name = "home/dish_confirm_delete.html"
    success_url = reverse_lazy("restaurant_kitchen:dish_list")
