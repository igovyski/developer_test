from . import models
from .api import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.


@api_view(['GET'])
def MultipleModels(request):
    survey_obj = models.Survey.objects.all()
    question_obj = models.SurveyQuestion.objects.all()
    alternative_obj = models.SurveyQuestionAlternative.objects.all()
    SurveySerializerObj = serializers.SurveySerializer(survey_obj, many=True)
    QuestionSerializerObj = serializers.SurveyQuestionSerializer(question_obj, many=True)
    AlternativeSerializerObj = serializers.SurveyQuestionAlternativeSerializer(alternative_obj, many=True)
    ResultModel = []

    for h, survey in enumerate(SurveySerializerObj.data):
        pesquisa = survey['id']
        ResultModel.append({f'Pesquisa {h + 1}': {'Nome Pesquisa': survey}})
        i = 1
        for question in QuestionSerializerObj.data:
            if question['survey'] == pesquisa:
                questao = question['id']
                ResultModel[h][f'Pesquisa {h + 1}'][f'Questão {i}'] = question
                j = 1
                for alternative in AlternativeSerializerObj.data:
                    if alternative['survey_question'] == questao:
                        ResultModel[h][f'Pesquisa {h + 1}'][f'Questão {i}'][f'Alternativa {j}'] = alternative
                    else:
                        j = 0
                    j += 1
            else:
                i = 0
            i += 1

    return Response(ResultModel)