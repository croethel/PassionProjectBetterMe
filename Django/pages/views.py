from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

class TrackerPageView(TemplateView):
    template_name = 'pages/tracker.html'


class StatsPageView(TemplateView):
    template_name = 'pages/stats.html'