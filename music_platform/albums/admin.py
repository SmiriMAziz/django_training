from django import forms
from django.contrib import admin

from .models import Album

# Register your models here.


class MyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MyForm, self).__init__(*args, **kwargs)
        self.fields['is_approved'].help_text = 'Approve the album if its name is not explicit'

    class Meta:
        model = Album
        exclude = ()


@admin.register(Album)
class Readonly(admin.ModelAdmin):
    form = MyForm
    readonly_fields = ["creation_datetime"]
