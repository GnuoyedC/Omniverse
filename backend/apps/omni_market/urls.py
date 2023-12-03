from django.urls import path
from . import views

app_name = 'omni_market'

urlpatterns = [
    path('market/', views.feature_view, name='feature'),
]