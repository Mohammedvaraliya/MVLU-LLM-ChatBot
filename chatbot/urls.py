from django.urls import path
from . import views
from .api.views import ChatbotView

urlpatterns = [
    path('', views.home, name='home'),
    path('query/', views.query, name='query'),
    path('apichatbot/', ChatbotView.as_view(), name='api_chatbot'),
]