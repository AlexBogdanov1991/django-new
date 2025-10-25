from rest_framework import serializers
from .models import Question, Choice

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        read_only_fields = ["id"]
        fields = [
            "id",
            "choice_text",
            "order"
        ]

class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = Question
        read_only_fields = ["id"]
        fields = [
            "id",
            "question_text",
            "pub_date",
            "choices"
        ]