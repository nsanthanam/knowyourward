from django.db import models
from django.core.validators import RegexValidator


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField()
    ward = models.CharField(max_length=10)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True)


SURVEY_LANGUAGES = (
    ('ENG', 'English'),
    ('TAM', 'Tamil')
)


class Survey(models.Model):
    survey_id = models.AutoField(primary_key=True)
    language = models.CharField(choices=SURVEY_LANGUAGES, max_length=5)


class SurveyResponse(models.Model):
    survey_id = models.ForeignKey(Survey)
    user_id = models.ForeignKey(User)
    time_taken = models.DateTimeField()


QUESTION_TYPES = (
    ('BOOL', 'Boolean'),
    ('RATE', 'Rating'),
    ('TEXT', 'Text')
)


class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    answer_type = models.CharField(choices=QUESTION_TYPES, max_length=5)


class Answer(models.Model):
    answer_id = models.AutoField(primary_key=True)
    question_id = models.ForeignKey(Question)
    survey_response_id = models.ForeignKey(SurveyResponse)
    text_answer = models.TextField(max_length=2048)
    bool_answer = models.BooleanField()
    rate_answer = models.IntegerField()


class SurveyQuestionMap(models.Model):
    id = models.AutoField(primary_key=True)
    question_id = models.ForeignKey(Question)
    survey_id = models.ForeignKey(Survey)
    text_question = models.TextField(max_length=1024)  # question text in the survey's language












