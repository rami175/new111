from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class ListPageView(TemplateView):
    template_name = "pages/list.html"