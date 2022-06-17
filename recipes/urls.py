from django.urls import path

from .views import CategoryTemplateView, IndexTemplateView, RecipeDetailView

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('category/<int:category_id>',
         CategoryTemplateView.as_view(), name='category'),
    path('detail/<int:pk>', RecipeDetailView.as_view(), name='detail'),

]
