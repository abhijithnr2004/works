from django.shortcuts import render
from django.utils import timezone

from rest_framework.generics import CreateAPIView,ListCreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework import authentication,permissions,serializers
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from QuizNest.serializers import UserSerializer,QuizSerializer,LanguageSerializer,QuestionSerializer,ChoiceSerializer,QuizAttemptSerializer,UserAnswerSerializer
from QuizNest.models import Quiz,Question,Languages,Choices,QuizAttempt,UserAnswer
from QuizNest.permissions import IsOwner



# Create your views here.
class SignupView(CreateAPIView) :

    permission_classes = [permissions.AllowAny]

    serializer_class = UserSerializer

class LanguageCreateListView(ListCreateAPIView) :

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = LanguageSerializer

    def get_queryset(self):

        return Languages.objects.all()
    

class QuizCreateListView(ListCreateAPIView) :

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = QuizSerializer

    def perform_create(self, serializer):


        if  serializer.validated_data.get("is_published"):

            raise serializers.ValidationError("Cannot publish quiz before adding atleast 5 questions")

        else :

            return serializer.save(created_by = self.request.user)
    
    def get_queryset(self):

        return Quiz.objects.all()
    
class QuizRetrieveView(RetrieveAPIView) :

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = QuizSerializer

    queryset = Quiz.objects.all()


class QuizUpdateDeleteView(UpdateAPIView,DestroyAPIView) :

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsOwner]

    serializer_class = QuizSerializer

    queryset = Quiz.objects.all()   

    def perform_update(self, serializer):

        quiz_id = self.kwargs.get("pk")

        quiz_instance = Quiz.objects.get(id=quiz_id)

        if quiz_instance.is_published :

            raise ValidationError("Cannot update published quizes")
        
        if serializer.validated_data.get("is_published") and quiz_instance.questions.count() < 5 :

            raise ValidationError("cannot publish quiz before adding atleast 5 questions")
        
        for question in quiz_instance.questions.all():

            if question.choices.count() < 2:

                raise ValidationError(f"Question '{question.title}' must have at least 2 choices")
            
            if not question.choices.filter(is_correct=True).exists :

                raise ValidationError(f"Question '{question.title}' must have at least 1 ansewer")

        serializer.save(quiz=quiz_instance)

    
        
    
class QuestionCreateView(CreateAPIView) :

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsOwner]

    serializer_class = QuestionSerializer

    def perform_create(self, serializer):

        quiz_id = self.kwargs.get("pk")

        quiz_instance = Quiz.objects.get(id=quiz_id)

        existing_question = quiz_instance.questions.filter(title=self.request.data.get("title"))

        if existing_question.exists():

            raise ValidationError("This question already exists for this quiz")    



        if self.request.user == quiz_instance.created_by:
            
            if quiz_instance.is_published :

                raise serializers.ValidationError("Cannot add questions to published quizes")

            serializer.save(quiz=quiz_instance)

        else:

            raise serializers.ValidationError("Cannot add questions to quiz created by other users")
        
class ChoiceCreateView(CreateAPIView) :

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsOwner]

    serializer_class = ChoiceSerializer

    def perform_create(self, serializer):

        question_id = self.kwargs.get("pk")

        question_instance = Question.objects.get(id=question_id)  

        existing_choice = question_instance.choices.filter(option=self.request.data.get("option"))

        if existing_choice.exists():

            raise ValidationError("This choice already exists for this question")    

        if self.request.user == question_instance.quiz.created_by:

            serializer.save(question=question_instance)

        else:

            raise ValidationError("Cannot add choices to questions created by other users")
        
class QuestionUpdateDeleteView(UpdateAPIView,DestroyAPIView) :


    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = QuestionSerializer  

    def perform_update(self, serializer):

        question_id = self.kwargs.get("pk")

        question_instance = Question.objects.get(id=question_id)

        if question_instance.quiz.created_by == self.request.user :

            if question_instance.quiz.is_published :

                raise ValidationError("Cannot update published quizes")

            serializer.save(question=question_instance)
        else :

            raise ValidationError("Cannot update questions created by other users")
        
    def get_queryset(self):

            question_id = self.kwargs.get("pk")

            question_instance = Question.objects.get(id=question_id)
    
            if self.request.user == question_instance.quiz.created_by:

                return Question.objects.all()
            
            else :

                raise ValidationError("Cannot delete questions created by other users")

class ChoiceUpdateDeleteView(UpdateAPIView,DestroyAPIView) :


    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = ChoiceSerializer

    queryset = Choices.objects.all()   

    def perform_update(self, serializer):

        Choice_id = self.kwargs.get("pk")

        Choice_instance = Choices.objects.get(id=Choice_id)

        if Choice_instance.question.quiz.created_by == self.request.user :
   
            if Choice_instance.question.quiz.is_published :

                raise ValidationError("Cannot update published quizes")

            serializer.save(Choice=Choice_instance)
        else :

            raise ValidationError("Cannot update questions created by other users")

    def get_queryset(self):

            choice_id = self.kwargs.get("pk")

            choice_instance = Choices.objects.get(id=choice_id)

            if choice_instance.question.quiz.is_published:

                raise ValidationError("cannot update choices in published quiz")
            
            else :
    
                if self.request.user == choice_instance.question.quiz.created_by:

                    return Choices.objects.all()
                
                else :

                    raise ValidationError("Cannot delete Choices created by other users")
        
class StartQuizView(CreateAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    queryset = QuizAttempt.objects.all()

    serializer_class = QuizAttemptSerializer

    def perform_create(self, serializer):

        return serializer.save(created_by=self.request.user, quiz_id=self.kwargs["quiz_id"])

class SubmitAnswerView(CreateAPIView,UpdateAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsOwner]

    queryset = UserAnswer.objects.all()

    serializer_class = UserAnswerSerializer


    def create(self, request, *args, **kwargs):

        attempt = QuizAttempt.objects.get(id=self.kwargs["pk"])

        if request.user != attempt.created_by:

            raise ValidationError("Cannot answer quiz started by another user")

        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        question = serializer.validated_data["question"]

        selected_choice = serializer.validated_data["selected_choice"]

        existing_answer = UserAnswer.objects.filter(
            attempt=attempt,
            question=question
        ).first()

        if existing_answer:
            existing_answer.selected_choice = selected_choice
            existing_answer.save()
            return Response({"message": "Answer updated"})

        serializer.save(attempt=attempt)
        return Response({"message": "Answer saved"})
        
class SubmitQuizView(UpdateAPIView):

    authentication_classes = [authentication.TokenAuthentication]
    
    permission_classes = [IsOwner]

    queryset = QuizAttempt.objects.all()

    def update(self, request, *args, **kwargs):

        attempt = QuizAttempt.objects.filter(id=self.kwargs["pk"]).first()

        if not attempt:
            raise ValidationError("Invalid attempt")

        if attempt.created_by != request.user:
            raise ValidationError("Invalid owner")

        if attempt.is_completed:
            raise ValidationError("Quiz already submitted")

        correct_count = attempt.answers.filter(
            selected_choice__is_correct=True
        ).count()

        attempt.score = correct_count
        attempt.is_completed = True
        attempt.completed_at = timezone.now()
        attempt.save()

        return Response({
            "message": "Quiz submitted successfully",
            "score": attempt.score
        })



        







