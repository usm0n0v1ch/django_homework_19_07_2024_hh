from django.urls import path

from app import views

urlpatterns = [
    path('vacancy_list/', views.vacancy_list, name='vacancy_list'),
    path('vacancy_detail/<int:vacancy_id>/', views.vacancy_detail, name='vacancy_detail'),
    path('resume_create/', views.resume_create, name='resume_create'),
    path('profile/', views.profile, name='profile'),
    path('resume_detail/<int:resume_id>/', views.resume_detail, name='resume_detail'),
    path('resume_edit/<int:resume_id>/', views.resume_edit, name='resume_edit'),
    path('resume_delete/<int:resume_id>/', views.resume_delete, name='resume_delete'),
    path('resume_list/', views.resume_list, name='resume_list'),
    path('vacancy_create', views.vacancy_create, name='vacancy_create'),
    path('vacancy/<int:vacancy_id>/respond/', views.respond_to_vacancy, name='respond_to_vacancy'),

]