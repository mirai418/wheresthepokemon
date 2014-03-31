from django.shortcuts import render
from pokemon.models import *
from django.shortcuts import *
# Create your views here.

def home(request):
    if request.method == "GET":
        p = Pokemon.objects.all()
        context = dict()
        context['all_pokemon'] = p
        return render(request, 'index.html', context)
