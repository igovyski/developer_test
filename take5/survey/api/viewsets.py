"""from rest_framework import viewsets
from survey.api import serializers
from survey import models


class SurveyViewSets(viewsets.ReadOnlyModelViewSet):
    queryset = models.Survey.objects.all().prefetch_related()
    serializer_class = serializers.SurveySerializer
"""