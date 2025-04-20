from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'publication_date', 'cover']
        labels = {
            'title': 'Title',
            'author': 'Author',
            'description': 'Description',
            'publication_date': 'Publication Date',
            'cover': 'Cover Image',
        }
