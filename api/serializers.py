
from django.contrib.auth.models import User
from django.db.models.base import Model
from rest_framework.serializers import ModelSerializer
from lessons.models import Attendance, Lesson, Message
from events.models import Event
from rest_framework import serializers

##Register 
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user
class UserSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'



class LessonSerializer(ModelSerializer):

    students = UserSerializer(many=True)
    class Meta:
        model = Lesson
        fields = '__all__'

class AttendanceSerializer(ModelSerializer):
   
    lesson = LessonSerializer(many=False)
    user_joined = UserSerializer(many=True)
    class Meta:
        model = Attendance
        fields = ['id', 'lesson', 'user_joined', 'date', 'date2', 'avaliable']


class MessagesSerializer(ModelSerializer):
    user = UserSerializer(many=False)
    class Meta:
        model = Message
        fields = '__all__'
        
class MessageSerializer(ModelSerializer):
 
   
    class Meta:
        model = Message
        fields = ('lesson',"user","text")
        
class EventSerializer(ModelSerializer):
    teacher = UserSerializer(many=False)
    students = UserSerializer(many=True)
   
    class Meta:
        model = Event
        fields = '__all__'