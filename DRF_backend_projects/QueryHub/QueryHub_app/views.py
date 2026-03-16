from django.shortcuts import render

from QueryHub_app.models import Query,Solution,Upvote
from QueryHub_app.serializers import UserSerializer,QuerySerializer,SolutionSerializer,UpvoteSerializer
from QueryHub_app.permissions import IsOwner

from rest_framework import permissions,authentication,serializers
from rest_framework.generics import CreateAPIView,ListCreateAPIView,RetrieveAPIView,DestroyAPIView

# Create your views here.

class SignupView(CreateAPIView) :

    permission_classes = [permissions.AllowAny]

    serializer_class = UserSerializer

class QueryCreateListView(ListCreateAPIView) :

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = QuerySerializer

    def perform_create(self, serializer):

        return serializer.save(created_by = self.request.user)

    def get_queryset(self):

        return Query.objects.all()
    
class SolutionCreateView(CreateAPIView) :


    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = SolutionSerializer

    def perform_create(self, serializer):

        id = self.kwargs.get("pk")

        question_instance = Query.objects.get(id=id)

        if question_instance.created_by == self.request.user :

            raise serializers.ValidationError("you cannot answer questions uploaded by you")    
        
        else :

            return serializer.save(question = question_instance,answered_by = self.request.user)
    
class QueryRetrieveView(RetrieveAPIView) :

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = QuerySerializer

    def  get_queryset(self):

        return Query.objects.filter(is_active="True")

class QueryDeleteView(DestroyAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsOwner]

    serializer_class = QuerySerializer

    def  get_queryset(self):

        return Query.objects.filter(is_active="True")
    
class UpvoteCtreateView(CreateAPIView) :

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = UpvoteSerializer

    def perform_create(self, serializer):

        id = self.kwargs.get("pk")

        answer_instance = Solution.objects.get(id=id)

        if answer_instance.answered_by == self.request.user :

            raise serializers.ValidationError("you cannot vote answers uploaded by you")    
        
        else :

            return serializer.save(answer = answer_instance,voted_by = self.request.user)
    




    







    

