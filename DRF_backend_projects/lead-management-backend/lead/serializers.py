from rest_framework import serializers

from django.contrib.auth.models import User

from lead.models import Lead


class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    

class LeadSerializer(serializers.ModelSerializer):

    class Meta:

        model = Lead
        fields = "__all__"
        read_only_fields = ['owner']