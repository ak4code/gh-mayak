from .models import Booking, Feedback
from rest_framework import serializers


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
