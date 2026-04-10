from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('add/', views.add_blog, name='add_blog'),
    path('edit/<int:id>/', views.edit_blog, name='edit_blog'),
    path('delete/<int:id>/', views.delete_blog, name='delete_blog'),
    path('register/', views.register, name='register'),
    path('upload_csv/', views.upload_csv, name='upload_csv'),
    path('api/blogs/', views.api_blog_list),
    path('api/add-blog/', views.api_add_blog),
]