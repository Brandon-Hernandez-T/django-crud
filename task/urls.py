from django.urls import path, include
from rest_framework import routers
from task import views

router = routers.DefaultRouter()
router.register(r'task', views.TaskView, 'tasks')

urlpatterns = [
    path('tasks', include(router.urls))
]