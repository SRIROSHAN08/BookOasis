from django.urls import path
from .views import *

urlpatterns=[
    path('all/',AllContribView.as_view()),
    path('<int:pk>',BookerDetailView.as_view(),name="booker_detail"),
]