
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    title = forms.CharField(max_length=100, required=True)
    author = forms.CharField(max_length=100, required=True)
    price = forms.DecimalField(min_value=0.0, max_digits=6, decimal_places=2, required=True)
    edition = forms.IntegerField(min_value=1, required=True)

    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'edition']
