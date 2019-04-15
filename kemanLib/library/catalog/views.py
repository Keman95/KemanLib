# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views import generic
from django.views.generic.list import ListView
from catalog.models import Book, Author, BookInstance, Genre

def index(request):
    """view function for home page"""
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status='a').count()  
    num_authors = Author.objects.count()
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }
    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):  
    model = Book
    paginate_by = 10

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        return context 

class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author

class AuthorDetailView(generic.DetailView):
    model = Author
    paginate_by = 2