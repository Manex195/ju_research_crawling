from django.urls import path
from . import views

urlpatterns = [
    path('author-search/', views.author_search, name='author_search'),
    path('', views.teacher_list, name='teacher_list'),
]