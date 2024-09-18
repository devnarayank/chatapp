from rest_framework import serializers
from .models import Room, Message

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model=Roomfields = '__all__'

class MessageSerializer(serializers.modelSerializer):
    class meta:
        model = Message
        fields = '__all__'