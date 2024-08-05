from django.db import models
import uuid

# Create your models here.

class Question(models.Model):
    content = models.CharField(max_length=2000, null=True, blank=True)
    image = models.FileField(upload_to="image", null=True)
    answer = models.CharField(max_length=5000, null=True, blank=True)
    
    class Meta:
        db_table = "questions"

class Answer(models.Model):
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE, related_field="question_answers")
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_field="user_answers")
    code = models.CharField(max_length=5000, null=True, blank=True)
    point = models.IntegerField(default=0)

    class Meta:
        db_table = "answers"
        
class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    session = models.UUIDField(max_length=200, default=uuid.uuid4)
    
    class Meta:
        db_table = "users"