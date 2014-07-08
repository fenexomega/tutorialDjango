from django.contrib import admin
from polls.models import Poll,Choice
# Register your models here.

class ChoiceInLine(admin.TabularInline):
	model = Choice
	extra = 3


class PollAdmin(admin.ModelAdmin):
	list_display = ('question','pub_date')
	fieldsets = [
	(None, {'fields':['question']}),
	("Date information", {'fields':['pub_date']})
	]
	inlines = [ChoiceInLine]
	list_filter = ['pub_date']

admin.site.register(Poll,PollAdmin)


