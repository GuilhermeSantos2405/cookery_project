from django.views.generic import TemplateView


class IndexTemplateView(TemplateView):
    template_name = 'recipes/templates/index.html'


class DetailTemplateView(TemplateView):
    template_name = 'recipes/templates/detail.html'
