# pages/urls.py
from django.urls import path
from .views import homePageView, aboutPageView, jesperPageView, homePost, results

urlpatterns = [
    path('', homePageView, name='home'),
    path('about/', aboutPageView, name='about'),
    path('jesper/', jesperPageView, name='jesper'),
    path('homePost/', homePost, name='homePost'),
    path('<int:choice>/results/', results, name='results'),

]
