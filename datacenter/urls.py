from django.urls import path
from datacenter import views

app_name = 'datacenter'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('course/', views.course, name='course')
]