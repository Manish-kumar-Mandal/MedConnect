from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_page, name='logout'),
    path('doctors/', views.doctors_page, name='doctors'),
    path('contact/', views.contact, name='contact'),
    path('doctorprofile/', views.doctor_profile_page, name='doctorprofile'),
    path('bookappointment/', views.appointment, name='bookappointment'),
    path('forgotpass/', views.forgot_page, name='forgotpass'),
]