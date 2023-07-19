# URL DE APLICACION


from django.urls import path
from .views import posts, articulos


urlpatterns = [
    path('posts/', posts, name='posts'),
    path('articulos', articulos, name='articulo'),

]