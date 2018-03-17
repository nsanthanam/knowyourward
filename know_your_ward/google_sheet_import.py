import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "know_your_ward.settings")

import django
django.setup()

from surveys.models import User, Question, Survey, SurveyQuestionMap, Answer, SurveyResponse

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('GOOGLE-KEY-XYZ.json', scope)

gc = gspread.authorize(credentials)
wks = gc.open("GOOGLE-SHEET-NAME").sheet1

list_of_rows = wks.get_all_values()
column_labels = list_of_rows.pop(0)

# Create or Get a survey
survey = Survey(survey=1, language=Survey.ENG)
survey.save()

question_text = column_labels[8]

question = Question(answer_type=Question.BOOL)
question.save()

survey_question_map = SurveyQuestionMap(question=question, survey=survey, text_question=question_text)
survey_question_map.save()

for row in list_of_rows:  # iterate over user responses
    ward = row[7]
    if ward.isdigit():
        ward_number = ward
    else:
        ward_number = -1

    user = User(ward=ward_number)
    user.save()

    response = row[8]
    survey_response = SurveyResponse(survey=survey, user=user)
    survey_response.save()
    answer = Answer(
        question=survey_question_map,
        survey_response=survey_response,
        bool_answer=True if response == "Yes" else False)
    answer.save()
