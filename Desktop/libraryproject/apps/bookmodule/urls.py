from django.urls import path
from django.urls import path, include
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
    path('lab9/task1/', views.task1Lab9, name='task1Lab9'),  # lab 9
    path('lab9/task2/', views.task2Lab9, name='task2Lab9'),  # lab 9
    path('lab9/task3/', views.task3Lab9, name='task3Lab9'),  # lab 9
    path('lab9/task4/', views.task4Lab9, name='task4Lab9'),  # lab 9
    
    path('lab9_part1/list', views.lab9_part1_listbooks ,name='lab9-list'),
    path('lab9_part1/add', views.lab9_part1_addbook ,name='lab9-add'),
    path('lab9_part1/edit/<int:book_id>', views.lab9_part1_editbook ,name='lab9-edit'),
    path('lab9_part1/delete/<int:book_id>', views.lab9_part1_deletebook ,name='lab9-delete'),
    path('lab9_part1/add-form/', views.lab9_part1_add_form ,name='lab9-add-form'),
    path('lab9_part1/edit-form/<int:book_id>', views.lab9_part1_edit_form ,name='lab9-edit-form'),


#lab 11 task 1
    path('list', views.list_students, name='list_students'),
    path('add/', views.add_student, name='add_student'),
    path('edit/<int:student_id>/', views.edit_student, name='edit_student'),
    path('delete/<int:student_id>/', views.delete_student, name='delete_student'),
    
    # lab 11 Task 2 URLs
    path('task2/list/', views.list_students2, name='list_students2'),
    path('task2/add/', views.add_student2, name='add_student2'),
    path('task2/edit/<int:student_id>/', views.edit_student2, name='edit_student2'),
    path('task2/delete/<int:student_id>/', views.delete_student2, name='delete_student2'), 
    #lab 11 task 3
    path('task3/add/', views.add_gallery_image, name='add_gallery_image'),
    path('task3/list/', views.list_gallery_images, name='list_gallery_images'),
 
    
]

    
  








