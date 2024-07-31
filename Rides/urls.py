from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/<int:user_id>/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('create_ride/', views.create_ride, name='create_ride'),
    path('ride_list/', views.ride_list, name='ride_list'),
    path('scam-info/', views.scam_info, name='scam_info'),
    path('carpool-bonus/', views.carpool_bonus_info, name='carpool_bonus_info'),
    path('delete_ride/<int:ride_id>/', views.delete_ride, name='delete_ride'),
]
