"""Jobs app URLs file"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('jobposts/', views.JobpostListView.as_view(), name='jobposts'),
    path('jobpost/<int:pk>/', views.JobpostDetailView.as_view(), name='jobpost'),
    path('jobpost/<int:pk>/update/', views.JobpostUpdateView.as_view(), name='update-jobpost'),
    path('jobpost/<int:pk>/delete/', views.JobpostDeleteView.as_view(), name='delete-jobpost'),
    path('jobpost/new/', views.JobpostCreateView.as_view(), name='create-jobpost')
]
