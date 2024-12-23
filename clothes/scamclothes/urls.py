from django.contrib.auth.views import (PasswordResetView,
                                       PasswordResetDoneView, PasswordResetCompleteView, PasswordResetConfirmView)
from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('flights/', views.flight, name='flights'),
    path('password-reset/', PasswordResetView.as_view(
         template_name='scamclothes/password/password_reset_form.html'),
         name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(
         template_name='scamclothes/password/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
         template_name='scamclothes/password/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(
         template_name='scamclothes/password/password_reset_complete.html'),
         name='password_reset_complete'),
    path('flight_post/<slug:slug>/', views.flight_post, name='flight_post'),
    path('search/', views.search_flights, name='search_flights'),
    path('about/', views.about, name='about'),
    path('bucket/add/<int:flight_id>/', views.add_to_bucket, name='add_to_bucket'),
    path('bucket/remove/<int:flight_id>/', views.remove_from_bucket, name='remove_from_bucket'),
    path('bucket/view/', views.view_bucket, name='view_bucket'),
    path('bucket/checkout/', views.checkout, name='checkout'),
    path('pay/<int:user_id>', views.pay, name='pay')
]
