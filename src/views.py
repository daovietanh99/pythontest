from rest_framework import viewsets
from src.models import Question, User
from src.serializers import QuestionSerializer, UserSerializer, LoginSerializer, FullUserSerializer, PointSerializer
from src.filters import QuestionFilter, UserFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from django.core.exceptions import PermissionDenied
import uuid
from django.shortcuts import render
from django.conf import settings


def index(request):
  return render(request, "index.html")

def login(request):
  return render(request, "login.html")

def signin(request):
  return render(request, "signin.html")


class QuestionView(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    filterset_class = QuestionFilter
    serializer_class = QuestionSerializer
    ordering = "id"


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    filterset_class = UserFilter
    serializer_class = UserSerializer
    ordering = "-point"
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @action(detail=False, url_path="login", serializer_class=LoginSerializer, methods=["post"])
    def login(self, request):
        login_serializer = LoginSerializer(data=request.data)
        login_serializer.is_valid(raise_exception=True)
        instance = User.objects.filter(username=login_serializer.validated_data["username"]).filter(password=login_serializer.validated_data["password"]).first()
        if not instance:
            raise PermissionDenied
        session = uuid.uuid4()
        user_serializer = FullUserSerializer(instance, data={"session": session}, partial=True)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()
        return Response(data={"session": session})
    
    @action(detail=False, url_path="add-point", serializer_class=PointSerializer, methods=["post"])
    def add_point(self, request):
        user = request.session["user"]
        point_serializer = PointSerializer(data=request.data)
        point_serializer.is_valid(raise_exception=True)
        instance = User.objects.filter(pk=user["id"]).first()
        if not instance:
            raise PermissionDenied
        user_serializer = FullUserSerializer(instance, data={"point": user['point'] + point_serializer.validated_data["point"]}, partial=True)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()
        return Response(data=user_serializer.validated_data)
      
    @action(detail=False, url_path="info", methods=["get"])
    def get_info(self, request):
        user = request.session["user"]
        return Response(data=user)