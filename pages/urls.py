from django.urls import path

from . import views

urlpatterns = [
    path('',views.mainpage),
    path('company/', views.company),
    path('login/', views.login_view),
    path('signup/', views.signup_view),
]