from django.contrib import admin
from .models import Survey, SurveyQuestion, SurveyQuestionAlternative

# Register your models here.

admin.site.register(Survey)
admin.site.register(SurveyQuestion)
admin.site.register(SurveyQuestionAlternative)