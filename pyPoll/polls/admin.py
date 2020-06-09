from django.contrib import admin
from .models import Question, Choice

admin.site.site_header = 'PyPoll Admin'
admin.site.site_title = 'PyPoll Admin Zone'
admin.site.index_title = 'Welcome to Poll Admin'

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3 # how many extra fields you want


class QuestionAdmin(admin.ModelAdmin):
    # This is a tuple. Takes in name, object. Requires hanging comma at end.
    fieldsets = [
        ( None, {'fields': ['question_text']} ), 
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ] 
    inlines = [ ChoiceInline ]


admin.site.register(Question, QuestionAdmin)