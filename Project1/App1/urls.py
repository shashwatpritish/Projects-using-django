from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="Home"),
    path('delete/<str:note>', views.delete, name="Delete"),
    path('update/<str:note>', views.update, name="Update"),
]