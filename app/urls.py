from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_news, name='all_news'),
    path('top/', views.top_news, name='top_news'),
    path('trending/', views.trending_news, name='trending_news'),
    path('science/', views.science_news, name='science_news'),
    path('entertainment/', views.entertainment_news, name='entertainment_news'),
    path('sports/', views.sports_news, name='sports_news'),
]
