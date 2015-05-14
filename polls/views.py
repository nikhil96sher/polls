from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Question
from django.template import RequestContext,loader
from django.shortcuts import render,get_object_or_404
from django.http import Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
# Create your views here.

#def login(request):
#	response="Welcome To the polls app!!"
#	return HttpResponse(response)

def index(request):
	latest_question_list=Question.objects.order_by('-pub_date')[:5]
	#template=loader.get_template('polls/index.html')
	context={'latest_question_list':latest_question_list}
	return render(request,'polls/index.html',context)

def details(request,question_id):
#	try:
#		question=Question.objects.get(id=question_id)
#	except Question.DoesNotExist:
#		raise Http404("Question doesn't exist")
	question=get_object_or_404(Question,pk=question_id)
	return render(request,'polls/detail.html',{'question':question})

def result(request,question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request,'polls/result.html', {'question': question})

def vote(request,question_id):
	p=get_object_or_404(Question,pk=question_id)
	selected_choice = p.choice_set.get(pk=request.POST['choice'])
	selected_choice.votes+=1
	selected_choice.save()
	return HttpResponseRedirect(reverse('polls:result',args=(p.id,)))

