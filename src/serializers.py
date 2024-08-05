from rest_framework import serializers

from src.models import Question, User, Answer

class QuestionSerializer(serializers.ModelSerializer):
    image = serializers.FileField()
    class Meta:
        model = Question
        fields = "__all__"

class ListUserSerializer(serializers.Serializer):
    name = serializers.CharField()
    total_points = serializers.IntegerField()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['session']
        
class FullUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["password"]

class SigninSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()
   
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        exclude = ["user"]

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"