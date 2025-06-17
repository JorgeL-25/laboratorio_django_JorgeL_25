from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Pokemon, Entrenador
from .forms import PokemonForm

def lista_pokemons(request):
    pokemons = Pokemon.objects.all()
    return render(request, 'pokemon/lista_pokemons.html', {'pokemons': pokemons})

def detalle_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, pk=pokemon_id)
    return render(request, 'pokemon/detalle_pokemon.html', {'pokemon': pokemon})

@login_required
def agregar_pokemon(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            pokemon = form.save(commit=False)
            pokemon.entrenador = request.user.entrenador
            pokemon.save()
            return redirect('lista_pokemons')
    else:
        form = PokemonForm()
    return render(request, 'pokemon/form_pokemon.html', {'form': form})

@login_required
def editar_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, pk=pokemon_id)
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('detalle_pokemon', pokemon_id=pokemon.id)
    else:
        form = PokemonForm(instance=pokemon)
    return render(request, 'pokemon/form_pokemon.html', {'form': form})

@login_required
def eliminar_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, pk=pokemon_id)
    if request.method == 'POST':
        pokemon.delete()
        return redirect('lista_pokemons')
    return render(request, 'pokemon/confirmar_eliminar.html', {'pokemon': pokemon})

def lista_entrenadores(request):
    entrenadores = Entrenador.objects.all()
    return render(request, 'pokemon/lista_entrenadores.html', {'entrenadores': entrenadores})