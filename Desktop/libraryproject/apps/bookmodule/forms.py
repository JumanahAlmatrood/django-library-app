
from django import forms
from .models import Book
from .models import Student,Student2,Address2,Gallery

class BookForm(forms.ModelForm):
    title = forms.CharField(max_length=100, required=True)
    author = forms.CharField(max_length=100, required=True)
    price = forms.DecimalField(min_value=0.0, max_digits=6, decimal_places=2, required=True)
    edition = forms.IntegerField(min_value=1, required=True)

    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'edition']

#lab11
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'address']
        
class Student2Form(forms.ModelForm):
    addresses = forms.ModelMultipleChoiceField(
        queryset=Address2.objects.all(),#manytomany
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model = Student2
        fields = ['name', 'addresses']

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['title', 'image']
