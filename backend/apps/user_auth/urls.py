from django.urls import path
from . import views

app_name = 'user_auth'

urlpatterns = [
    path('auth/', views.feature_view, name='feature'),
]