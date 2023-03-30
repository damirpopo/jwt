from .views import *
from django.urls import path


urlpatterns = [
    path('book/',BookList.as_view()),
    path('book/<int:pk>',BookDestroyUpdate.as_view()),
    path('orderbook/',OrderBookListCreate.as_view()),
]