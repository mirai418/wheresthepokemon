from django.shortcuts import render
from pokemon.models import *
from django.shortcuts import *
# Create your views here.

def home(request):
	context = dict()
	if request.method == "GET":
		p = Pokemon.objects.all().order_by("-vote")
		context['all_pokemon'] = p
		return render(request, 'index.html', context)
	if (request.method == "POST"):
		print request.POST
		try:
			name = request.POST["name"]
			link = request.POST["link"]
		return render(request, 'index.html', context)

