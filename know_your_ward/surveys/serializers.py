from rest_framework import serializers, viewsets

from .models import SurveyQuestionMap


class QuestionSerializer(serializers.ModelSerializer):
    responses = serializers.SerializerMethodField()

    class Meta:
        model = SurveyQuestionMap

        depth = 1
        fields = ('text_question', 'survey', 'question', 'responses')

    def get_responses(self, obj):
        from collections import Counter

        response = Counter([answer.bool_answer for answer in obj.answer_set.all()])
        return response


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = SurveyQuestionMap.objects.all()
    serializer_class = QuestionSerializer
