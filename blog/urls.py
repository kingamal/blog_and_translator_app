from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomeView.as_view(), name='home_view'),
    path('<slug:slug>', views.BlogView.as_view(), name='blog_view'),
]