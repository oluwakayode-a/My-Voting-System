from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('add_aspirant/', views.add_aspirant, name='add_aspirant'),
    path('asp_post', views.asp_post, name='asp_post'),
    path('vote/<slug:slug>', views.vote, name='vote'),
]