from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views


router = routers.DefaultRouter()
router.register('tasks', views.TaskView, 'task')

urlpatterns = [
    path('sentry-debug/', trigger_error), # Новый маршрут.
    path('admin/', admin.site.urls),
]
