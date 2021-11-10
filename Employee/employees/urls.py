"""mtTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views
urlpatterns = [
  url(r'^$', views.show),
   url(r'^show', views.show),
   url(r'^emp', views.emp),
   url(r'^edit/(?P<id>\w+)', views.edit),
   url(r'^update/(?P<id>\w+)', views.update),
   url(r'^delete/(?P<id>\w+)', views.destroy),
   url(r'^register/', views.register_request,name="register"),
   url(r'^login/', views.login_request,name="login"),
   url(r'^logout/', views.logout_request, name= "logout")
    
]