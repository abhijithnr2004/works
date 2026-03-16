from rest_framework import serializers

from QueryHub_app.models import User,Query,Solution,Upvote

class UserSerializer(serializers.ModelSerializer) :

    class Meta :

        model = User

        fields = ['username','email','password','phone']

        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):

        return User.objects.create_user(**validated_data)


    
class QuerySerializer(serializers.ModelSerializer) :

    class Meta :

        model = Query

        fields = "__all__"

        read_only_fields = ['created_by']

    answers = serializers.SerializerMethodField()

    def get_answers(self,object) :

        answer_objects = object.answers.all()

        serializer_instance = SolutionSerializer(answer_objects,many=True)

        return serializer_instance.data

    

class SolutionSerializer(serializers.ModelSerializer) :

    question = serializers.StringRelatedField(read_only = True)

    class Meta :

        model = Solution

        fields = "__all__"

        read_only_fields = ['question','answered_by']

    votes = serializers.SerializerMethodField()

    def get_votes(self,object) :

        return Upvote.objects.filter(answer = object).count()
    
    voters = serializers.SerializerMethodField()

    def get_voters(self,object) :

        vote_object = Upvote.objects.filter(answer = object)

        return vote_object.values_list("voted_by__username",flat=True)



class UpvoteSerializer(serializers.ModelSerializer) :

    class Meta :

        model = Upvote

        fields = "__all__"

        read_only_fields = ['answer','voted_by','voted_at']

    