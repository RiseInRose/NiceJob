"""NiceJob URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from job_web.views import index2
from myusers import views

from django.contrib.auth import urls as auth_urls

urlpatterns = [
    url(r'^job_web/', include('job_web.urls')),
    url(r'^myusers/', include('myusers.urls')),
    url(r'^admin/', admin.site.urls),
    # url(r'^accounts/', include('users.urls')),
    # 将 auth 应用中的 urls 模块包含进来
    url(r'^myusers/', include('django.contrib.auth.urls')),
    url(r'^$', index2),

]
