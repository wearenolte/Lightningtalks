# coding: utf-8
import json

from annoying.decorators import render_to, ajax_request
from django.http import HttpResponse
from django.shortcuts import redirect

from .models import Human, Talks
from .forms import TalksForm


@render_to('home.html')
def home(request, cicle=None, topic=None):
	if cicle is None:
		cicle = Talks.objects.get(pk=1).cicle
	if topic and topic != '0':
		talks = Talks.objects.filter(cicle=cicle, topic=topic).order_by('-date')
	else:
		talks = Talks.objects.filter(cicle=cicle).order_by('-date')
	current = Human.objects.get(is_active=True, current=True)
	form = TalksForm(initial={'human': current})
	return { 'talks' : talks, 'current' : current, 'form': form }


@ajax_request
def current(request):
	if request.method == 'POST':
		h = Human.objects.get(pk=request.POST.get('human'))
		t = request.POST.get('topic')
		n = request.POST.get('name')
		l = request.POST.get('link')
		cicle = Talks.objects.get(pk=1).cicle
		talk = Talks(human=h, topic=t, name=n, link=l, cicle=cicle)
		talk.save()
		response_data = {}
		response_data['result'] = 'Create post successful!'
		return {'success' : 1}


@render_to('nominee.html')
def nominee(request):
	nominees = Human.objects.filter(is_active=True, lightning=True)
	if request.POST:
		current = Human.objects.get(is_active=True, current=True)
		current.current = False
		current.save()
		victim = Human.objects.get(pk=request.POST.get('user'))
		victim.current = True
		victim.lightning = False
		victim.save()
		return redirect('home')

	return {'nominees': nominees}


@render_to('victim.html')
def victim(request):
	current = Human.objects.get(is_active=True, current=True)
	current.current = False

	available = Human.objects.filter(is_active=True, lightning=True).order_by('?')
	victim = available.first()
	victim.current = True
	victim.lightning = False
	current.save()
	victim.save()

	m = ''
	print(available.count())
	if available.count() == 0:
		humans = Human.objects.filter(is_active=True)
		cycle = Talks.objects.get(pk=1)
		m = f'End of cycle #{cycle.cicle}'
		cycle.cicle = cycle.cicle + 1
		cycle.save()
		for h in humans:
			h.lightning = True
			h.save()

	return { 'current' : current, 'victim': victim, 'message': m }
