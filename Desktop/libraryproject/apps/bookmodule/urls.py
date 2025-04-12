from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path("html5/links", views.html5_links, name="books.html5.links"),#task 1 lab 5
    path('html5/text/formatting/', views.formatting_page, name="books.formatting"),#task 2 lab 5
    path('html5/listing/', views.listing_page, name="books.listing"),#task 3 lab5
    path('html5/tables/', views.tables_page, name="books.tables"),# task 4 lab 5
    path('search', views.search_books, name="books.search"),#lab6
    path('simple/query', views.simple_query),#lab7
    path('complex/query', views.complex_query),#lab7
    path('lab8/task1/', views.task1, name='task1'),#lab 8
    path('lab8/task2/', views.task2, name='task2'),#lab 8
    path('lab8/task3/', views.task3, name='task3'),#lab 8
    path('lab8/task4/', views.task4, name='task4'),#lab 8
    path('lab8/task5/', views.task5, name='task5'),#lab 8
    path('lab8/task7/', views.task7, name='task7'),#lab 8





]
