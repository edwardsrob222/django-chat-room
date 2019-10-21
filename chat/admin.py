from django.contrib import admin

# Register your models here.
from .models import Comment, Chat

admin.site.register(Comment)
admin.site.register(Chat)
