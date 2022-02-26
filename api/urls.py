from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.getRoutes, name="routes"),
    path("notes/", views.getNotes, name="notes"),
    path("notes/create", views.createNote, name="create-note"),
    path("notes/<str:id>/", views.getNote, name="note"),
    path("notes/update/<str:id>", views.updateNote, name="update-note"),
    path("notes/delete/<str:id>", views.deleteNote, name="delete-note"),
]
