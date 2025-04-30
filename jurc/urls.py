from django.urls import path
from . import views

urlpatterns = [
    path('author-search/', views.author_search, name='author_search'),
    path('', views.teacher_list, name='teacher_list'),
    path('teachers/<int:pk>/', views.teacher_detail, name='teacher_detail'),
]