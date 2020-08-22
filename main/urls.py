from django.urls import path
from main import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('question/<int:pk>',login_required(views.Question.as_view()), name='question'),
]