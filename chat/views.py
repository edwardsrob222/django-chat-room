from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Chat, Comment


class ChatListView(generic.ListView):
    model = Chat


class ChatDetailView(generic.DetailView):
    model = Chat


class CommentCreateView(generic.CreateView):
    model = Comment
    fields = ('text',)

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.chat_id = self.kwargs['pk']
        return super().form_valid(form)
