from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from .models import Book, Student ,Department, Course,Student2, Address2,Gallery
from django.db.models import Q
from django.db.models import Count, Sum, Avg, Max, Min
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from .forms import BookForm,StudentForm,Student2Form,GalleryForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book

#lab11 task 3
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def add_gallery_image(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_gallery_images')
    else:
        form = GalleryForm() # بدون شي
    return render(request, 'bookmodule/add_gallery_image.html', {'form': form})
@login_required(login_url='login')
def list_gallery_images(request):
    images = Gallery.objects.all()# انسى هذه 
    return render(request, 'bookmodule/list_gallery_images.html', {'images': images})
#lab11 task 2 Students with Many-to-Many Addresses

def list_students2(request):
    students = Student2.objects.all()
    return render(request, 'bookmodule/list_students2.html', {'students': students})

def add_student2(request):
    if request.method == 'POST':
        form = Student2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_students2')
    else:
        form = Student2Form()
    return render(request, 'bookmodule/add_student2.html', {'form': form})

def edit_student2(request, student_id):
    student = Student2.objects.get(id=student_id)
    if request.method == 'POST':
        form = Student2Form(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list_students2')
    else:
        form = Student2Form(instance=student)
    return render(request, 'bookmodule/edit_student2.html', {'form': form, 'student': student})

def delete_student2(request, student_id):
    student = Student2.objects.get(id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('list_students2')
    return render(request, 'bookmodule/delete_student2.html', {'student': student})


#11 task 1
def list_students(request):
    students = Student.objects.all()
    return render(request, 'bookmodule/list_students.html', {'students': students})
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForm()
    return render(request, 'bookmodule/add_student.html', {'form': form})
def edit_student(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForm(instance=student)
    return render(request, 'bookmodule/edit_student.html', {'form': form, 'student': student})


def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('list_students')
    return render(request, 'bookmodule/delete_student.html', {'student': student})




#lab10
def lab9_part1_listbooks(request):
    books = Book.objects.all
    return render(request, 'bookmodule/lab9_list.html',{'books':books})

def lab9_part1_addbook(request):# اول مايفتح الصفحه get يروح ل render بعده redirect
    if request.method =='POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        edition = request.POST.get('edition')
        Book.objects.create(title=title, author=author, price=price,edition=edition)

        return redirect('lab9-list') # نفس name في urls 
    return render(request, 'bookmodule/lab9_add.html')


def lab9_part1_editbook(request,book_id):# بس نحفظ الفرق بينه وبين ادد 
    book = Book.objects.get(id=book_id)
    if request.method =='POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        edition = request.POST.get('edition')

        book.title = title
        book.author = author
        book.price = price
        book.edition = edition
        book.save()
        return redirect('lab9-list')
    return render(request, 'bookmodule/lab9_edit.html',{'book':book})


def lab9_part1_deletebook(request,book_id):
    book = Book.objects.get(id=book_id)
    if request.method =='POST':
        book.delete()
        return redirect('lab9-list')  
    return render(request, 'bookmodule/lab9_delete.html',{'book':book})   



def lab9_part1_add_form(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lab9-list')
    else:
        form = BookForm()

    return render(request, 'bookmodule/lab9_add_form.html', {'form': form})


def lab9_part1_edit_form(request, book_id):
    book = Book.objects.get(id=book_id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('lab9-list')
    else:
        form = BookForm(instance=book)

    return render(request, 'bookmodule/lab9_edit_form.html', {'form': form, 'book': book})
########

#lab9
def task1Lab9(request):
    departments = Department.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/task1Lab9.html', {'departments': departments})

def task2Lab9(request):
    courses = Course.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/task2Lab9.html', {'courses': courses})

# لازم افهم اللي داخل وش
def task3Lab9(request):
    department = Department.objects.annotate(student_count=Min('student__id'))
    return render(request, 'bookmodule/task3Lab9.html', {'department': department})

def task4Lab9(request):
    departments = Department.objects.annotate(student_count=Count('student')).filter(student_count__gt=2).order_by('-student_count')
    return render(request, 'bookmodule/task4Lab9.html', {'departments': departments})

####





def task7(request):#lab 8
    stats = Student.objects.values('address__city').annotate(student_count=Count('id'))
    return render(request, 'bookmodule/task7.html', {'stats': stats})

def task5(request):#lab 8
    stats = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        average_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/task5.html', {'stats': stats})


def task4(request):#lab 8
    books = Book.objects.all().order_by('title')  # ترتيب تصاعدي (A → Z)
    # لو تبين ترتيب تنازلي (Z → A)، تكتبين: .order_by('-title')
    return render(request, 'bookmodule/task4.html', {'books': books})

def task3(request):#lab8
    books = Book.objects.filter(
        ~Q(edition__gt=3) & ~(
            Q(title__icontains="co") | Q(author__icontains="co")
        )
    )
    return render(request, 'bookmodule/task3.html', {'books': books})

def task2(request):#lab8
    books = Book.objects.filter(
        Q(edition__gt=3) & (Q(title__icontains="co") | Q(author__icontains="co"))
    )
    return render(request, 'bookmodule/task2.html', {'books': books})

def task1(request):#lab 8
    books = Book.objects.filter(Q(price__lte=80))
    return render(request,'bookmodule/task1.html', {'books': books})


def simple_query(request):#lab 7
    mybooks = Book.objects.filter(title__icontains='and')  # <- multiple objects
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})

def complex_query(request):#lab 7
    mybooks = Book.objects.filter(author__isnull=False)\
                          .filter(title__icontains='and')\
                          .filter(edition__gte=2)\
                          .exclude(price__lte=100)[:10]

    if len(mybooks) >= 1:
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
    else:
        return render(request, 'bookmodule/index.html')



def html5_links(request):#task 1
    return render(request, "bookmodule/links.html")

def formatting_page(request):# task 2
    return render(request, "bookmodule/formatting.html")

def listing_page(request): # task 3
    return render(request, "bookmodule/listing.html")

def tables_page(request):# task 4
    return render(request, "bookmodule/tables.html")

from django.shortcuts import render

from django.shortcuts import render

def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]

def search_books(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        books = __getBooksList()
        newBooks = []

        for item in books:
            contained = False
            if isTitle and string in item['title'].lower():
                contained = True
            if not contained and isAuthor and string in item['author'].lower():
                contained = True

            if contained:
                newBooks.append(item)

        return render(request, 'bookmodule/bookList.html', {'books': newBooks})
    
    return render(request, 'bookmodule/search.html')



def index(request):
    return render(request, "bookmodule/index.html")

def list_books(request):
    return render(request, "bookmodule/list_books.html")

def viewbook(request, bookId):
    return render(request, "bookmodule/one_book.html")

def aboutus(request):
    return render(request, "bookmodule/aboutus.html")






# def index(request):
#     name = request.GET.get("name") or "world!"
#     return render(request, "bookmodule/index.html", {"name": name})  

# def index2(request, val1):
#     if not isinstance(val1, int):  
#         return HttpResponseBadRequest("Error: expected val1 to be an integer")

#     return HttpResponse(f"value1 = {val1}")

# def viewbook(request, bookId):
#     # assume that we have the following books somewhere (e.g. database)
#     book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
#     book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
#     targetBook = None
#     if book1['id'] == bookId: targetBook = book1
#     if book2['id'] == bookId: targetBook = book2
#     context = {'book':targetBook} # book is the variable name accessible by the template
#     return render(request, 'bookmodule/show.html', context)














# from django.http import HttpResponse
# def index(request):
#     name = request.GET.get("name") or "world!"  
#     return HttpResponse("Hello, "+name) 

# def index2(request, val1 = 0):  
#     return HttpResponse("value1 = "+str(val1))

