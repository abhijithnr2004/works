from rest_framework import serializers

from django.contrib.auth.models import User
from django.utils import timezone

from eventmanagement.models import Event

import datetime


class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only':True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class EventSerializer(serializers.ModelSerializer):

    class Meta:

        model = Event
        fields = "__all__"
        read_only_fields = ['owner', 'created_date', 'updated_date']

    
    def validate_patient_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Event name cannot be empty or just whitespace.")
        return value

    def validate_Event_date(self, value):
        if value < datetime.date.today():
            raise serializers.ValidationError("The Event date cannot be in the past.")
        return value

    def validate_Event_time(self, value):
        if not value:
            raise serializers.ValidationError("Event time is required.")
        return value