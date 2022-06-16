from django.urls import path

from .views import DetailTemplateView, IndexTemplateView

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('detail', DetailTemplateView.as_view(), name='detail'),

]
