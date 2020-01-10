from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from ..models import Question
from ..serializers import QuestionSerializer

from ..models import Choice
from ..serializers import ChoiceSerializer

class QuestionViewSet(viewsets.ModelViewSet):

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_fields = ('question_text',)

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
    )
    filter_fields = ('votes','question_id',)
    search_fields = ('choice_text',)