from django import forms
from .models import *
from django.core.exceptions import ValidationError

class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ['title', 'uniq']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'uniq': forms.TextInput(attrs={'class': 'form-control'})
            }


    def clean_tag(self):
        new_tag = self.cleaned_data['uniq'].lower()

        if  Tag.objects.filter(uniq__iexact=new_tag.count()):
            raise ValidationError()

        return new_tag

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['title', 'uniq', 'body', 'tags']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'uniq': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'})
            }

        def clean_tag(self):
            new_tag = self.cleaned_data['uniq'].lower()
            return new_tag
