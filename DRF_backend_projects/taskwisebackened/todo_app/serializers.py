from rest_framework import serializers

from todo_app.models import Task

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields=["id","username","email","password"]
        read_only_fields=["id"]


class TaskSerializer(serializers.ModelSerializer):

    class Meta:

        model = Task

        fields="__all__"

        read_only_fields=["id","owner","created_at"]
