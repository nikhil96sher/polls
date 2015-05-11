from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Question
from django.template import RequestContext,loader
from django.shortcuts import render,get_object_or_404
from django.http import Http404
# Create your views here.
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
	response="You are seeing the result of Question no %s."%question_id
	return HttpResponse(response)
def vote(request,question_id):
	response="Want to vote for Question no. %s?"% question_id;
	return HttpResponse(response)
