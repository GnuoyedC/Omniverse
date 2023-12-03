from django.urls import path
from . import views

app_name = 'user_collection'

urlpatterns = [
    path('collection/', views.feature_view, name='feature'),
]