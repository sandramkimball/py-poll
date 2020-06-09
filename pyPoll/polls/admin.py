from django.contrib import admin
from .models import Question, Choice

admin.site.site_header = 'PyPoll Admin'
admin.site.site_title = 'PyPoll Admin Zone'
admin.site.index_title = 'Welcome to Poll Admin'

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = []
    inlines = [ ChoiceInline ]

admin.site.register(Question, QuestionAdmin)