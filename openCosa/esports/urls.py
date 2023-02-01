from django.urls import path

from . import views 

urlpatterns = [
    path("", views.index, name="esports_raiz"),
    
]