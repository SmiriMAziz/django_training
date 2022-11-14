from django import forms
from django.contrib import admin
from .models import Album, Song
from django.forms import ValidationError
from django.forms.models import BaseInlineFormSet

# Register your models here.


class MyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MyForm, self).__init__(*args, **kwargs)
        self.fields['is_approved'].help_text = 'Approve the album if its name is not explicit'

    class Meta:
        model = Album
        exclude = ()


class RequiredInlineFormSet(BaseInlineFormSet):
    """
    Generates an inline formset that is required
    """

    def _construct_form(self, i, **kwargs):
        """
        Override the method to change the form attribute empty_permitted
        """
        form = super(RequiredInlineFormSet, self)._construct_form(i, **kwargs)
        form.empty_permitted = False
        return form


class SongInline(admin.StackedInline):
    model = Song
    extra = 1
    formset = RequiredInlineFormSet


@admin.register(Album)
class Readonly(admin.ModelAdmin):
    form = MyForm
    readonly_fields = ["created"]
    inlines = [
        SongInline,
    ]

    def save_model(self, request, obj, form, change):

        super().save_model(request, obj, form, change)


admin.site.register(Song)
