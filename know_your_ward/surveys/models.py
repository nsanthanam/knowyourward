from django.db import models
from django.core.validators import RegexValidator


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField()
    ward = models.CharField(max_length=10)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True)


class Survey(models.Model):
    ENG = 'English'
    TAM = 'Tamil'

    SURVEY_LANGUAGES = (
        (ENG, 'English'),
        (TAM, 'Tamil')
    )
    survey = models.AutoField(primary_key=True)
    language = models.CharField(choices=SURVEY_LANGUAGES, max_length=5)


class SurveyResponse(models.Model):
    survey = models.ForeignKey(Survey)
    user = models.ForeignKey(User)


class Question(models.Model):
    BOOL = 'BL'
    RATE = 'RT'
    TEXT = 'TX'

    QUESTION_TYPES = (
        (BOOL, 'Boolean'),
        (RATE, 'Rating'),
        (TEXT, 'Text')
    )

    question_id = models.AutoField(primary_key=True)
    answer_type = models.CharField(choices=QUESTION_TYPES, max_length=5)


class Answer(models.Model):
    answer_id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question)
    survey_response = models.ForeignKey(SurveyResponse)
    text_answer = models.TextField(max_length=2048, null=True, blank=True)
    bool_answer = models.NullBooleanField(null=True, blank=True)
    rate_answer = models.IntegerField(null=True, blank=True)


class SurveyQuestionMap(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question)
    survey = models.ForeignKey(Survey)
    text_question = models.TextField(max_length=1024)  # question text in the survey's language














