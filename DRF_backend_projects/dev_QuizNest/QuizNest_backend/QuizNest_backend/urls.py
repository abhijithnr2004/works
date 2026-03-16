"""
URL configuration for QuizNest_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from QuizNest import views
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.SignupView.as_view()),
    path('token/',ObtainAuthToken.as_view()),
    path('quiz/',views.QuizCreateListView.as_view()),
    path('get-quiz/<int:pk>/',views.QuizRetrieveView.as_view()),
    path('quiz/<int:pk>/',views.QuizUpdateDeleteView.as_view()),
    path('language/',views.LanguageCreateListView.as_view()),
    path('questions/<int:pk>/',views.QuestionCreateView.as_view()),
    path('choice/<int:pk>/',views.ChoiceCreateView.as_view()),
    path('questionsUpdateorDelete/<int:pk>/',views.QuestionUpdateDeleteView.as_view()),
    path('choiceUpdateorDelete/<int:pk>/',views.ChoiceUpdateDeleteView.as_view()),
    path("quiz/<int:quiz_id>/start/",views.StartQuizView.as_view()),
    path("attempt/<int:pk>/answer/",views.SubmitAnswerView.as_view()),
    path("attempt/<int:pk>/submit/", views.SubmitQuizView.as_view()),

]
