from django.urls import path
from . import views

urlpatterns = [
    path('', views.data_list, name='excel_home'),
    path('upload/', views.upload_excel, name='upload_excel'),
    path('data/', views.data_list, name='data_list'),
]