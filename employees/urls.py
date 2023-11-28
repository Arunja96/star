from django.urls import path

from . import views

urlpatterns = [
    path("", views.employees, name="employees"),
    path("employeeform/", views.employeeform, name="employeeform"),
    path("viewrecord/<int:pk>", views.view_record, name="viewrecord"),
    path("deleterecord/<int:pk>", views.delete_record, name="deleterecord"),
    path("updaterecord/<int:pk>", views.update_record, name="updaterecord"),
]