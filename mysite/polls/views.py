 # -*- coding: utf-8 -*-
from django.shortcuts import render, Http404 , get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from polls.models import Poll, Choice
from django.views import generic


class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_poll_list'

	def get_queryset(self):
		"""Retorne as 5 últimas enquentes publicadas"""
		return Poll.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Poll
	template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
	model = Poll
	template_name = 'polls/results.html'

def vote(request, poll_id):
	poll = get_object_or_404(Poll,pk=poll_id)
	try:
		selected_choice = poll.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Mostre novamente a parte de votos
		return render(request,'polls/detail.html',{
			'poll':poll,
			'error_message':'Você não fez uma escolha.'
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Sempre retorne um HttpResponseRedirect depois de sucetivamente mexer
		# com dados POST. Isso previne os dados de serem postados duas vezes se
		# o usuário apertar o botão voltar do navegador.
		return HttpResponseRedirect(reverse('polls:results',args=(poll.id,)))  