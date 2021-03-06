from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class Chat(models.Model):
    name = models.CharField(max_length=255)
    # member = models.ManytoManyField(User, related_name='chats')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('chat:chat_list')




class Comment(models.Model):
    text = models.TextField()
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


    def get_absolute_url(self):
        return reverse('chat:chat_detail', args=(self.chat_id,))
