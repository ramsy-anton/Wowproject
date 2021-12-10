from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('genre/<str:genre>', views.genre, name='genre'),
    path('edit/<int:post_id>', views.edit, name='edit'),
    path ('post/', views.post, name='create'),
]