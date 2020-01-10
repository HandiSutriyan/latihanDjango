from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status

from ..models import Question
from ..serializers import QuestionSerializer

from ..models import Choice
from ..serializers import ChoiceSerializer

class QuestionViewSet(viewsets.ModelViewSet):

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
    )
    filter_fields = ('question_text',)
    search_fields = ('question_text','id',)

    #override function for method post
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # self.perform_create(serializer)
        # headers = self.get_success_headers(serializer.data)
        serializer.save(created_by=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
    )
    filter_fields = ('votes','question_id',)
    search_fields = ('choice_text',)