"""
URL configuration for lead_management project.

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

from lead.views import UserSignUpView, LeadCreateList, LeadRetrieveUpdateDeleteView, LeadSummaryView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', UserSignUpView.as_view()),
    path('lead/', LeadCreateList.as_view()),
    path('lead/<int:pk>/', LeadRetrieveUpdateDeleteView.as_view()),
    path('summary/', LeadSummaryView.as_view()),
]
