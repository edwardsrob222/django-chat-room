from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Chat, Comment

#list of chat rooms
class ChatListView(generic.ListView):
    model = Chat
    template_name = 'chat/chat_list.html'

#specific chat
class ChatDetailView(generic.DetailView):
    model = Chat
    template_name = 'chat/chat_detail.html'

#adding comment
class CommentCreateView(generic.CreateView):
    model = Comment
    fields = ('text',)

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.chat_id = self.kwargs['pk']
        return super(CommentCreateView, self).form_valid(form)


#deleting comment
class CommentDeleteView(generic.DeleteView):
    model = Comment
    fields = ('text',)


class ChatCreateView(generic.CreateView):
    model = Chat
    fields = '__all__'
    template_name = 'chat/chat_create.html'



# class Add_Member(request, pk):
#     chat = get_object_or_404(Question, pk=pk)
#     chat.instance.created_by = self.request.user
