from urllib import request
from django import forms
from django.core.files.base import ContentFile
from django.utils.text import slugify
from .models import Image


class ImageCreateForm(forms.Form):
    class Meta:
        model = Image
        fields = ('title', 'url', 'description')
        widgets = {
            'url': forms.HiddenInput,
        }

    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('the given url does not match valid image extension')
        return url