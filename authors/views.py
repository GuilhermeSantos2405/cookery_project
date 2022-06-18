from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView, UpdateView
from django.views.generic.edit import CreateView
from recipes.models import Recipe


class AuthorRecipesView(ListView):
    template_name = 'authors/templates/author_recipe.html'
    context_object_name = 'authors_recipes'
    model = Recipe
    paginate_by = 4

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(author__id=self.kwargs.get(
            'author_id'), is_published=True)
        return qs
