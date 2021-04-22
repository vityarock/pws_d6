# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .forms import BookForm
from django.urls import reverse_lazy
from p_library.models import Book, Publisher, Reader


class BookCreate(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('p_library:book_list')
    template_name = 'book_edit.html'


class BookUpdate(UpdateView):
    model = Book
    success_url = reverse_lazy('p_library:book_list')
    fields = ['title', 'cover', 'price', 'copy_count']
    template_name = 'book_edit.html'


class BookRead(ListView):
    model = Book
    template_name = 'book_list.html'


def books_list(request):
    books = Book.objects.all()
    return HttpResponse(books)

def index(request):
    template = loader.get_template('index.html')
    books = Book.objects.all()
    books_count = books.count()
    biblio_data = {
        "title": "мою библиотеку",
        "books_count": books_count,
        "books": books,
    }
    return HttpResponse(template.render(biblio_data))

def pub_list(request):
    template = loader.get_template('publishers.html')
    publishers = Publisher.objects.all()
    books = Book.objects.all()
    pub_data = {
        "publishers": publishers,
        "books": books,
    }
    return HttpResponse(template.render(pub_data))

def reader_list(request):
    template = loader.get_template('readers.html')
    readers = Reader.objects.all()
    books = Book.objects.all()
    read_data = {
        "readers": readers,
        "books": books,
    }
    return HttpResponse(template.render(read_data))
