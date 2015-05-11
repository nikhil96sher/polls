from django.conf.urls import patterns,url
from polls import views
urlpatterns=patterns('',url(r'^$',views.index,name='index'),url(r'^(?P<question_id>\d+)/$',views.details,name='detail'),url(r'^(?P<question_id>\d+)/result/$',views.result,name='reslt'),url(r'^(?P<question_id>\d+)/vote/$',views.vote,name='vote'),)
