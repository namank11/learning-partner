# Defines urlpatterns for learning_partners

from django.urls import path
from . import views

app_name = 'learning_partners'

urlpatterns = [
    path('', views.index, name='index'),
    path('/topics', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]