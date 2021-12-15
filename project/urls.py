from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('project/new/', views.projectCreateView, name="new_project")
]