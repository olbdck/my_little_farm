from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name='main'),
    path('farmers/', views.farmers, name='farmers'),
    path('farmers/details/<int:id>', views.details, name='details'),
    # path('testing/', views.testing, name='testing'),
]
