
from django.urls import path
from . import views

# all routes related to account login / register
urlpatterns = [
    path('', views.auth_page, name='auth'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout')
]
