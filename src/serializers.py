from rest_framework import serializers

from src.models import Question, User

class QuestionSerializer(serializers.ModelSerializer):
    image = serializers.FileField()
    class Meta:
        model = Question
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['session']
        
class FullUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
class PointSerializer(serializers.Serializer):
    point = serializers.IntegerField(default = 0)