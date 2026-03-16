"""
URL configuration for doctor_appoinment_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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

from appointment.views import UserSignUpView, AppointmentCreateListView, AppointmentReatrievUpdateDeleteView

from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', UserSignUpView.as_view()),
    path('token/', ObtainAuthToken.as_view()),
    path('appointments/', AppointmentCreateListView.as_view()),
    path('appointments/<int:pk>/', AppointmentReatrievUpdateDeleteView.as_view()),

]
