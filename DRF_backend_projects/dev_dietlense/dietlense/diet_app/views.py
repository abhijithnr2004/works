from django.shortcuts import render

# Create your views here.


from rest_framework.generics import CreateAPIView,RetrieveAPIView,UpdateAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView

from diet_app.serializers import UserSerializer,UserProfileSerializer,FoodLogSerializer

from diet_app.permissions import IsOwner,ProfileRequired,HasFoodLog

from diet_app.utility_fun import daily_calorie_consumption

from diet_app.models import UserProfile,User,FoodLog

from rest_framework import permissions,authentication,serializers,views

from django.utils import timezone

from rest_framework.response import Response

from django.db.models import Sum

from diet_app.get_diet_plan import generate_kerala_diet_plan




class SignUpView(CreateAPIView):

    serializer_class = UserSerializer

class UserProfileCreateView(CreateAPIView) :

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = UserProfileSerializer

    def perform_create(self, serializer):
        
        # validated_data = serializer.validated_data

        # cal = daily_calorie_consumption(
        #     height=validated_data.get("height"),
        #     weight=validated_data.get("weight"),
        #     age=validated_data.get("age"),
        #     gender=validated_data.get("gender"),
        #     activity_level=float(validated_data.get("activity_level",1.2))
        # )

        serializer.save(owner = self.request.user)

class UserProfileRetrieveUpdateView(RetrieveAPIView,UpdateAPIView) :

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsOwner,ProfileRequired] 

    serializer_class = UserProfileSerializer

    queryset = UserProfile.objects.all()

class UserRetrieveView(RetrieveAPIView) :

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsOwner]

    serializer_class = UserSerializer

    queryset = User.objects.all()

class FoodlogCreateListView(ListCreateAPIView) :

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = FoodLogSerializer

    def perform_create(self, serializer):

        return serializer.save(owner = self.request.user)
    
    def get_queryset(self):

        return FoodLog.objects.filter(owner = self.request.user)
    
class FoodlogRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView) :

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsOwner]

    serializer_class = FoodLogSerializer

    queryset = FoodLog.objects.all()

class FoodlogSummaryView(views.APIView) :

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes =[ HasFoodLog,ProfileRequired,permissions.IsAuthenticated]

    def get(self,request,*args,**kwargs) :

        cur_date = timezone.now().date()
        
        qs = FoodLog.objects.filter(owner = request.user,created_at__date = cur_date)

        consumed = qs.values('calories').aggregate( calorie_total = Sum('calories'))

        meal_type_total = qs.values("meal_type").annotate(total = Sum("calories"))

        context = {
            "target": request.user.profile.bmr,
            "consumed today" :  consumed.get('calorie_total',0),
            "Meal type summary" :  meal_type_total,
            "remaining" : request.user.profile.bmr -consumed.get('calorie_total',0),
        }

        return Response(data=context)
    
class DietplanView(views.APIView) :

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated,ProfileRequired]

    def post(self,request,*args,**kwargs) :

        goal = request.data.get("goal")

        age = request.user.profile.age

        weight = request.user.profile.weight

        gender = request.user.profile.gender

        target_weight = request.data.get("target_weight")

        duration = request.data.get("duration")

        diet_plan = generate_kerala_diet_plan(goal=goal,age=age,weight=weight,gender=gender,target_weight=target_weight,duration=duration)

        return Response(data=diet_plan)






        
        

    



   

    