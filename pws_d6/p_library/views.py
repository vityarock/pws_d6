# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .forms import ImageForm
from django.urls import reverse_lazy
from p_library.models import Book, Publisher, Reader


class BookUpdate(UpdateView):
    model = Book
    success_url = reverse_lazy('p_library:books_list')
    fields = ["title", "ISBN", "description", "year_release", "price", "copy_count"]
    template_name = 'book_edit.html'


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

def book_image_upload(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        book.cover = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
        return redirect('/index/')
    else:
        form = ImageForm()
