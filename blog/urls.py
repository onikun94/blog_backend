from django.urls import path
from blog import views
from .views import *

urlpatterns = [
    path('',ListTitle.as_view()),
    path('<str:pk>/',OnlyBlog.as_view()),
    path('all/',ListBlog.as_view())
]