from django.urls import path

from . import views

urlpatterns = [
    path("", views.teams, name="teams"),
    path("teamsform/", views.teamsform, name="teams_form"),
    path("viewteam/<int:pk>", views.view_role, name="viewteam"),
    path("deleteteam/<int:pk>", views.delete_role, name="deleteteam"),
    path("updateteam/<int:pk>", views.update_role, name="updateteam"),
]