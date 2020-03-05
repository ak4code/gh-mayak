from .models import Booking, Feedback
from rest_framework import serializers


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('id', 'name', 'city', 'text', 'created_at',)


class FeedbackSerializer(serializers.ModelSerializer):
    feedback = serializers.PrimaryKeyRelatedField(queryset=Feedback.objects.all(), allow_null=True)
    answers = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Feedback
        fields = ('id', 'name', 'city', 'text', 'feedback', 'created_at', 'answers')

    def get_answers(self, instance):
        answers = instance.answers.all().order_by('created_at')
        return AnswerSerializer(answers, many=True).data
