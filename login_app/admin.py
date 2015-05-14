from django.contrib import admin
from login_app.models import user,profile
# Register your models here.

#admin.site.register(profile)
class profileinline(admin.StackedInline):
	model=profile
	extra=1
class useradmin(admin.ModelAdmin):
	fieldsets=[('User Details',{'fields':['username','email','password']})]
	inlines=[profileinline]
admin.site.register(user,useradmin)
