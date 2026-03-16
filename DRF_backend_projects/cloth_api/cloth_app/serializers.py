from rest_framework import serializers
from .models import Clothing


class ClothingSerializers(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)

    name = serializers.CharField()

    brand = serializers.CharField(allow_blank=True)

    category = serializers.CharField()

    size = serializers.CharField()

    color = serializers.CharField()

    price = serializers.IntegerField()

    stock = serializers.IntegerField()

    created_at = serializers.DateTimeField(read_only=True)


    def validate(self, data):

        price = data.get("price")
        stock = data.get("stock")
        color = data.get("color")

        # color only alphabets
        if not color.replace(" ","").isalpha():
            raise serializers.ValidationError("Color should contain alphabets only")


        return data
    
class UserSerializer(serializers.Serializer) :

    username = serializers.CharField()

    first_name = serializers.CharField()

    last_name = serializers.CharField()

    email = serializers.EmailField()

    password = serializers.CharField()

