from django.urls import path

from .views import HomePageView, AboutPageView, TrackerPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('tracker/', TrackerPageView.as_view(), name='tracker'),
]
