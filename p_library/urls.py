from django.contrib import admin
from django.urls import path
from .views import BookRead, BookCreate, BookUpdate

app_name = "p_library"

urlpatterns = [

    path('book/', BookRead.as_view(), name='book_list'),
    path('book/create/', BookCreate.as_view(), name='book_edit'),
    path('book/<int:pk>/', BookUpdate.as_view(), name='book_edit')
]
