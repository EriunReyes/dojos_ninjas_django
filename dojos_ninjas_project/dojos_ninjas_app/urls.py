from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('dojos_route', views.dojos),
    path('ninjas_route', views.ninjas),
    path('destroy_dojos/<int:dojos_id>', views.destroy),
]