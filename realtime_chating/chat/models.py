from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    name = models.charField(max_length=100, unique=True)

class Message(models.Model):
    room = models.ForeignKey(Room, related_name="messages", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DataTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

# Create your models here.
