from django.conf.urls import url
from . import views

app_name = 'myusers'
urlpatterns = [
    url(r'^register/', views.register, name='register'),
    url(r'^$', views.index, name='index')
]