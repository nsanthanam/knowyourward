from rest_framework import viewsets

from .serializers import QuestionSerializer
from .models import SurveyQuestionMap


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = SurveyQuestionMap.objects.all()
    serializer_class = QuestionSerializer
