from django.urls import path


from . import views

app_name = 'chat'

urlpatterns = [
    # pk is the pk of the room you want to add the comment to
    path('<int:pk>/comment/new/', views.CommentCreateView.as_view(), name='add_comment'),
    path('<int:pk>/', views.ChatDetailView.as_view(), name='chat_detail'),
    #chat_list is home page
    path('', views.ChatListView.as_view(), name='chat_list'),
    # pk is the pk of the comment you want to delete
    path('<int:pk>/delete/', views.CommentDeleteView.as_view(), name='delete_comment'),
]
