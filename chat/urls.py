from django.urls import path


from . import views

app_name = 'chats'

urlpatterns = [
    path('<int:pk>/comment/new/', views.CommentCreateView.as_view(), name='add_comment'),
    path('<int:pk>/', views.ChatDetailView.as_view(), name='chat_detail'),
    path('', views.ChatListView.as_view(), name='chat_list'),
]
