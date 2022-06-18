from django.contrib.auth import views as auth_views
from django.urls import path

from .views import AuthorRecipesView

urlpatterns = [
    path('recipes/<int:author_id>',
         AuthorRecipesView.as_view(), name='author_recipes'),
]
