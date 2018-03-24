from rest_framework import serializers
from collections import Counter

from .models import SurveyQuestionMap


class QuestionSerializer(serializers.ModelSerializer):
    responses = serializers.SerializerMethodField()

    class Meta:
        model = SurveyQuestionMap

        depth = 1
        fields = ('text_question', 'survey', 'question', 'responses')

    def get_responses(self, obj):
        request = self.context['request']
        ward = request.query_params.get('ward', None)
        if ward:
            queryset = obj.answer_set.filter(survey_response__user__ward=ward)
        else:
            queryset = obj.answer_set.all()

        if obj.question.answer_type == 'BL':
            response = Counter([answer.bool_answer for answer in queryset])
        elif obj.question.answer_type == 'RT':
            response = Counter([answer.rate_answer for answer in queryset])
        else:
            response = {}
        return response
