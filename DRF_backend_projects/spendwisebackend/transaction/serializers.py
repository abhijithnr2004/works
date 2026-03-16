from rest_framework import serializers

from django.contrib.auth.models import User

from transaction.models import Expense

class UserSerializer(serializers.ModelSerializer) :

    class Meta :

        model = User

        fields = ["id","username","email","password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class ExpenseSerializer(serializers.ModelSerializer) :

    owner = serializers.SerializerMethodField()

    greetings = serializers.SerializerMethodField()

    

    class Meta :

        model = Expense

        fields = "__all__"

        read_only_fields = ['id','created_at','owner']

    def get_greetings(self,obj):

        return "Good morning"
    
    def get_owner(self,obj) :

        object_owner = obj.owner

        serializer_instance = UserSerializer(object_owner)

        return serializer_instance.data
        
        