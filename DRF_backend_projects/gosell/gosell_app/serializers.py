from rest_framework import serializers

from django.contrib.auth.models import User

from gosell_app.models import Vehicle

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = User

        fields = ['id', 'username', 'email', 'password']

        read_only_fields = ['id']

class Vehicleserializer(serializers.ModelSerializer):

    class Meta:

        model = Vehicle

        fields = "__all__"

        read_only_fields = ['id', 'owner']