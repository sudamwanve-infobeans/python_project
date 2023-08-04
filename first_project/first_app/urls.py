from django.urls import path
from first_app import views

urlpatterns = [
    path('', views.index,name="index"),
    path('help/', views.help,name="help"),
    path('gallery/', views.gallery,name="gallery"),
]