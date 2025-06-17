from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pokemons, name='lista_pokemons'),
    path('agregar/', views.agregar_pokemon, name='agregar_pokemon'),
    path('<int:pokemon_id>/', views.detalle_pokemon, name='detalle_pokemon'),
    path('<int:pokemon_id>/editar/', views.editar_pokemon, name='editar_pokemon'),
    path('<int:pokemon_id>/eliminar/', views.eliminar_pokemon, name='eliminar_pokemon'),
    path('entrenadores/', views.lista_entrenadores, name='lista_entrenadores'),
]