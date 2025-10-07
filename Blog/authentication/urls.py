from django.urls import path
from .views import *
from posts.views import *

urlpatterns=[
    path('',AllBooksView.as_view()),
    path('logout/',Logoutuser),
    path('register/',Register),
    path('login/',LoginPage),
]