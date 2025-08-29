from django.urls import path
from . import views

urlpatterns = [
    path('external/', views.get_external_api),
    path('create/', views.create_post),
]
