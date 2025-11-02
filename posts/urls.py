from django.urls import path
from .views import *

urlpatterns=[
    path('book/',AllBooksView.as_view()),
    path('<int:pk>',BookDetailView.as_view(),name='book_detail'),
    path('weather/',WeatherView.as_view(),name='weather'),
]