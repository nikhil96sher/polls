from django.contrib import admin
from polls.models import Question
from polls.models import Choice
# Register your models here.
class ChoiceInline(admin.TabularInline):
	model = Choice
	
class Questionadmin(admin.ModelAdmin):
	list_display=('question_text','pub_date')
	inlines=[ChoiceInline]
	list_filter=['pub_date']
	search_fields=['question_text']
admin.site.register(Question,Questionadmin)
