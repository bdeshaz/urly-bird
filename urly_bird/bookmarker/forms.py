from django import forms
from django.forms import URLInput
from .models import Bookmark


class BookmarkForm(forms.ModelForm):
    class Meta:
        model = Bookmark
        fields = ('url',)

        widgets = {'url': URLInput(attrs={'placeholder': "Paste URL Here"})}
