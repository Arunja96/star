from django.urls import path

from . import views

urlpatterns = [
    path("", views.roles, name="roles"),
    path("roleform/", views.roleform, name="roles_form"),
    path("viewrole/<int:pk>", views.view_role, name="viewrole"),
    path("deleterole/<int:pk>", views.delete_role, name="deleterole"),
    path("updaterole/<int:pk>", views.update_role, name="updaterole"),
]