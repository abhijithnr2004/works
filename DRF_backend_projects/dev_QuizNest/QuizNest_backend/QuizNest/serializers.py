from rest_framework import serializers
from QuizNest.models import User,Languages,Quiz,Question,QuizAttempt,UserAnswer,Choices
from django.utils import timezone
from django.db import transaction

class UserSerializer(serializers.ModelSerializer) :

    class Meta :

        model = User

        fields = ['username','email','password','phone']

        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):

        return User.objects.create_user(**validated_data)
    
class LanguageSerializer(serializers.ModelSerializer):

    class Meta:

        model = Languages

        fields = "__all__"
    
class QuizSerializer(serializers.ModelSerializer):

    language = serializers.StringRelatedField()

    created_by = serializers.StringRelatedField()

    question = serializers.StringRelatedField()


    class Meta:

        model = Quiz

        fields = "__all__"

        read_only_fields = ['created_by']

    questions = serializers.SerializerMethodField()

    def get_questions(self,obj) :
        
        try :

            question_objects = obj.questions.all()

            serializer = QuestionSerializer(question_objects,many=True)

            return serializer.data
        
        except Exception as e :

            raise serializers.ValidationError(e)

    total_questions = serializers.SerializerMethodField()

    def get_total_questions(self, obj):

        try :

            return obj.questions.count()
        
        except :

            return False
    
    def update(self, instance, validated_data):

        if instance.is_published:

            raise serializers.ValidationError("Published quizes cannot be edited")
        
        return super().update(instance, validated_data)
    
class QuestionSerializer(serializers.ModelSerializer):

    class Meta:

        model = Question

        fields = ['id', 'title', 'choices',"has_minimum_choices"]

        read_only_fields = ["has_minimum_choices"]

    choices = serializers.SerializerMethodField()

    def get_choices(self,obj) :
        
        choice_object = obj.choices.all()

        serializer = ChoiceSerializer(choice_object,many = True)

        return serializer.data
    
    has_minimum_choices  = serializers.SerializerMethodField()

    def get_has_minimum_choices(self,obj) :

        return obj.choices.count() >= 2
    
class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:

        model = Choices

        fields = "__all__"

        read_only_fields = ['question']

class QuizAttemptSerializer(serializers.ModelSerializer):

    

    class Meta:

        model = QuizAttempt

        fields ="__all__"

        read_only_fields = ["score", "is_completed", "started_at", "completed_at","created_by","quiz"]

        answers = serializers.SerializerMethodField()

    def get_answers(self,obj) :
        
        answer_object = obj.answers.all()

        serializer = UserAnswerSerializer(answer_object,many = True)

        return serializer.data

    
class UserAnswerSerializer(serializers.ModelSerializer):

    class Meta:

        model = UserAnswer

        fields = "__all__"

        read_only_fields = ["attempt"]

        unique_together = ('attempt', 'question')

    def validate(self, data):

        question = data["question"]

        choice = data["selected_choice"]

        # Check if choice belongs to question
        if choice.question != question:

            raise serializers.ValidationError("Selected choice does not belong to this question")

        return data




    

    


        



    



    






