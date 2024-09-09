from django.urls import path

from user import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.log_out, name='logout'),
]
