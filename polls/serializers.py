from rest_framework import serializers

from user.serializers import UserSerializer
from .models import Question
from .models import Choice

class QuestionSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(required = False)

    class Meta:
        model = Question
        fields = ('__all__')

class QuestionDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('id','question_text','pub_date',)

class ChoiceSerializer(serializers.ModelSerializer):
    question = QuestionDetailSerializer(required=False)

    class Meta:
        model = Choice
        fields = ('__all__')