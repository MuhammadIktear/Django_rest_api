"""
URL configuration for django_rest_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from drapi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # path('aiinfo/',views.aiquest_info),
    # path('aiinfo/<int:pk>/',views.aiquest_inst),
    path('AiquestList/',views.AiquestList.as_view(),name='AiquestList'),
    path('AiquestDetails/<int:pk>/',views.AiquestDetail.as_view(),name='AiquestDetails'),    
    # path('AiquestCreate/',views.AiquestCreate.as_view(),name='AiquestCreate'),
    # path('AiquestCreate/<int:pk>/',views.AiquestCreate.as_view(),name='AiquestCreate'),    
    # path('aicreate/',views.aiquest_create,name='aicreate'),
    # path('aicreate/<int:pk>/',views.aiquest_create,name='aicreate'),
    
]
