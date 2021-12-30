from django.shortcuts import render
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

import api
from .serializers import AttendanceSerializer, LessonSerializer, MessageSerializer
from lessons.models import Lesson, Attendance, Message

from api import serializers


@api_view(['GET'])
def getLessons(request):
    lessons = Lesson.objects.all()
    serializer = LessonSerializer(lessons,many= True)
    return Response(serializer.data)

@api_view(['GET'])
def getLesson(request, id):
    lessons = Lesson.objects.get(id = id)
    
    serializer = LessonSerializer(lessons,many= False)
    return Response(serializer.data)

@api_view(['POST'])
def createLesson(request):
    data = request.data

    lesson = Lesson.objects.create(
        teacher = data['teacher'],
        name = data['name'],
        description = data['description'] 
    )
    serializer = LessonSerializer(lesson, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateLesson(request, id):
    data = request.data
    lesson = Lesson.objects.get(id =id)
   

    serializer = LessonSerializer(lesson, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteLesson(request,id):
    lesson = Lesson.objects.get(id =id)
    lesson.delete()
    return Response("Ders silindi!")


@api_view(['GET'])
def getAttendances(request):
    attendances = Attendance.objects.all()
    serializer = AttendanceSerializer(attendances,many= True)
    return Response(serializer.data)

@api_view(['GET'])
def getMessages(request,id):
    messages = Message.objects.get(id=id)
    serializer = MessageSerializer(messages,many= False)
    return Response(serializer.data)