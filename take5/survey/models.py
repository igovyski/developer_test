from django.db import models

# Create your models here.


class Survey(models.Model):
    survey_text = models.CharField(max_length=200)

    def __str__(self):
        return self.survey_text


class SurveyQuestion(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    survey_question = models.CharField(max_length=200)

    def __str__(self):
        return self.survey_question


class SurveyQuestionAlternative(models.Model):
    survey_question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)
    survey_question_alternative = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.survey_question_alternative


class SurveyUserAnswer(models.Model):
    survey_question = models.ForeignKey(SurveyQuestionAlternative, on_delete=models.CASCADE)
    survey_user_answer = models.CharField(max_length=200)
