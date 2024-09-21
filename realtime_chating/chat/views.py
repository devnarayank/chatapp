from rest_framework import generics
from .models import Room, Message
from django.views.generic import TemplateView
from .serializers import RoomSerializer, MessageSerializer

class RoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class MessageList(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class IndexView(TemplateView):
    template_name = 'chat.html'