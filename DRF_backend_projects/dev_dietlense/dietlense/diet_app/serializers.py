

from rest_framework import serializers

from diet_app.models import User,UserProfile,FoodLog


class UserSerializer(serializers.ModelSerializer):


    class Meta:

        model = User

        fields=["id","username","email","phone","password","profile"]

        extra_kwargs = {"password":{"write_only":True}}

        # read_only_fields=["id","password"]

    profile = serializers.SerializerMethodField()

    def get_profile(self,obj) :
        
        try :
            profile_object = UserProfile.objects.get(owner = obj)

            serializer = UserProfileSerializer(profile_object)

            return serializer.data

        except :

            return None

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class UserProfileSerializer(serializers.ModelSerializer) :

    class Meta :

        model = UserProfile
        fields = "__all__"
        read_only_fields = ['owner','bmr']

class FoodLogSerializer(serializers.ModelSerializer) :

    class Meta :

        model = FoodLog

        fields = "__all__"

        read_only_fields = ['owner','created_at']

