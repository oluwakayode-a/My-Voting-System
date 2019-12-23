from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='user_system/login.html'), name='login'),
    path('logout/', views.log_voter_out, name='logout'),
    path('add_user/', views.add_user, name='add_user')
]
