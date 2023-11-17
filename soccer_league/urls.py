from django.urls import path, include
from rest_framework import routers
from soccer_league import views

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryView, 'categories')
router.register(r'teams', views.TeamView, 'teams')
router.register(r'players', views.PlayerView, 'players')

urlpatterns = [
    path('', include(router.urls))
]