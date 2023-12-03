from django.urls import path
from . import views

app_name = 'omni_catalog'

urlpatterns = [
    path('catalog/', views.feature_view, name='feature'),
]