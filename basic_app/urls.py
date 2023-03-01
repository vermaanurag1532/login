
from django.urls import path
from basic_app import views

# TEMPLATE URLS!

urlpatterns = [
    path('register/', views.register, name="register"),
]
