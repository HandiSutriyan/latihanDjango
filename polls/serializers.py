from rest_framework import serializers
from django.contrib.auth.models import User

from user.serializers import UserSerializer
from .models import Question
from .models import Choice

class QuestionSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(required = False)
    created_by_id = serializers.IntegerField(write_only=True, required=False, allow_null=True)

    class Meta:
        model = Question
        fields = (
            'id',
            'question_text',
            'pub_date',

            'created_by_id',
            'created_by',
        )
    #override function for method post
    def create(self, validated_data):

        created_by_id = validated_data.get("created_by_id")
        validated_data.pop("created_by_id", None)

        q = Question(**validated_data)

        #relate to user
        # user = User.objects.filter(id=created_by_id).first()
        # q.created_by = user
        q.save()

        return q
       

class QuestionDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('id','question_text','pub_date',)

class ChoiceSerializer(serializers.ModelSerializer):
    question = QuestionDetailSerializer(required=False)

    class Meta:
        model = Choice
        fields = ('__all__')