from rest_framework import serializers

from poll_app.models import User, Poll, Choice, Vote


class UserSerializer(serializers.ModelSerializer):

    # owner = serializers.StringRelatedField(read_only=True)

    class Meta:

        model = User
        fields = ['username', 'email', 'password', 'phone']
        extra_kwargs = {'password':{'write_only':True}}

    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    



class PollSerializer(serializers.ModelSerializer):

    class Meta:

        model = Poll
        fields = "__all__"
        read_only_fields = ['owner']

    choices = serializers.SerializerMethodField()

    vote_count = serializers.SerializerMethodField(read_only=True)

    def get_choices(self, obj):

        choice_objects = obj.choices.all()

        serializer_instance = ChoiceSerializer(choice_objects, many=True)

        return serializer_instance.data
    
    def get_vote_count(self,object) :

        return Vote.objects.filter(poll_object = object).count()


class ChoiceSerializer(serializers.ModelSerializer):

    poll_object = serializers.StringRelatedField(read_only=True)

    class Meta:

        model = Choice
        fields = "__all__"
        read_only_fields = ['poll_object']

    vote_count = serializers.SerializerMethodField(read_only = True)

    def get_vote_count(self,object) :

        return Vote.objects.filter(choice_object = object).count()
    
    voters = serializers.SerializerMethodField(read_only = True)

    def get_voters(self,object) :

        vote_object = Vote.objects.filter(choice_object = object)

        return vote_object.values_list("owner__username",flat=True)




class VoteSerializer(serializers.ModelSerializer):

    poll_object = serializers.StringRelatedField(read_only=True)

    class Meta:

        model = Vote
        fields = "__all__"
        read_only_fields = ['poll_object', 'owner']