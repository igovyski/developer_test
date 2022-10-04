from rest_framework import serializers
from survey import models


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Survey
        fields = ['id', 'survey_text']


class SurveyQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SurveyQuestion
        fields = ['id', 'survey_question', 'survey']


class SurveyQuestionAlternativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SurveyQuestionAlternative
        fields = ['id', 'survey_question_alternative', 'votes', 'survey_question']


class CombinedSerializer(serializers.ModelSerializer):
    survey = SurveySerializer()
    question = SurveyQuestionSerializer()
    alternative = SurveyQuestionAlternativeSerializer()

    class Meta:
        model = models.Survey
        fields = '__all__'

