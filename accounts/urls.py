from django.urls import path


from . import views

app_name = 'accounts'

urlpatterns = [
    path('profile_detail/', views.ProfileDetailView.as_view(), name='profile_detail'),
    path('profile/', views.ProfileCreateView.as_view(), name='profile'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]
