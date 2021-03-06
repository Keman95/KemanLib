from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^', views.index, name = 'index'),
    url(r'^books/', views.BookListView.as_view(), name = 'books'),
    url(r'^book/<int:pk>', views.BookDetailView.as_view(), name = 'book-detail'),
    url(r'^author', views.AuthorListView.as_view(), name = 'author'),
    url(r'^author/<int:pk>', views.AuthorDetailView.as_view(), name = 'author-detail' )
]

