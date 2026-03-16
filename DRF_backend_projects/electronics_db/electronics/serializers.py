from rest_framework.serializers import ModelSerializer

from django.contrib.auth.models import User

from electronics.models import ElectronicProduct

class UserSerializer(ModelSerializer) :

    class Meta : 

        model = User

        fields = ['id','username','email','password']

        read_only_fields = ['id']

class ElectronicProductSerializer(ModelSerializer) :

    class Meta :
        
        model = ElectronicProduct

        fields = "__all__"

        read_only_fields = ['id','owner']


