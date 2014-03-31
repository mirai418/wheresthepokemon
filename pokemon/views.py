from django.shortcuts import render, redirect
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
		try:
			name = request.POST["name"]
			link = request.POST["link"]
		except:
			context['all_pokemon'] = p
			return render(request, 'index.html', context)
		if (name != "" and link != ""):
			Pokemon.objects.create(name=name, link=link)
		p = Pokemon.objects.all().order_by("-vote")
		context['all_pokemon'] = p
		return render(request, 'index.html', context)

def vote(request, pk):
	print pk
	if (request.method == "POST"):
		try:
			p = Pokemon.objects.get(pk=pk)
			vote = request.POST["vote"]
			cur = p.vote
			print cur
			p.vote = cur + int(vote)
			p.save()
			return redirect('/')
		except:
			return redirect('/')
	else:
		return redirect('/')
