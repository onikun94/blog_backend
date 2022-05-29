from django.urls import path
from blog import views
from .views import *

urlpatterns = [
    path('',ListAll.as_view()),
    path('<str:pk>/',OnlyBlog.as_view()),
]