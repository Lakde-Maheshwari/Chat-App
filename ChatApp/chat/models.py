from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class ChatGroup(models.Model):
    group_name = models.CharField(max_length=100)

    def __str__(self):
        return self.group_name  

class GroupMessage(models.Model):
    group = models.ForeignKey(ChatGroup, on_delete=models.CASCADE, related_name='chat_messages')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=300,blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    File = models.FileField(upload_to='files/', blank=True, null=True)

    def __str__(self):
        return f'{self.author.username}: {self.body}'
    
    class Meta:
        ordering = ['-created']

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=300, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    group = models.ManyToManyField(ChatGroup,related_name="group_members")
    display_name = models.CharField(max_length = 50)

    def __str__(self):
        return f'{self.user.username} Profile'
