"""hausaufagenTabelle5d URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

import ha.views as ha_views

urlpatterns = [
	path ('admin/', admin.site.urls),
	path ('', ha_views.index),
	path ('details/<int:id>/', ha_views.details, name='details'),
	path ('add/', ha_views.add),
	path ('edit/<int:id>/', ha_views.edit),
	path ('del/<int:id>/', ha_views.delete),
	path ('deletion_complete/<int:id>', ha_views.deletion_copmplete),
]
