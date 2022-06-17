import os

from django.contrib.auth.mixins import LoginRequiredMixin as LRM
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, TemplateView

""" from .forms import RecipeRegisterView """
from .models import Recipe

PER_PAGE = int(os.environ.get('PER_PAGE', 6))


class ListViewBase(ListView):
    context_object_name = 'recipes_list'
    model = Recipe
    paginate_by = PER_PAGE


class IndexTemplateView(ListViewBase):
    template_name = 'recipes/templates/pages/index.html'

    def get_queryset(self):
        return Recipe.objects.filter(is_published=True).order_by('?')


class CategoryTemplateView(ListViewBase):
    template_name = 'recipes/templates/pages/category.html'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(category__id=self.kwargs.get(
            'category_id'), is_published=True)
        return qs


class RecipeDetailView(DetailView):
    template_name = 'recipes/templates/pages/detail.html'
    login_url = reverse_lazy('login')
    model = Recipe

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(is_published=True)
        return qs
