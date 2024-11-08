from django import forms
from task.models import TodoTask


class Datainput(forms.DateTimeInput):
    input_type='date'

class Taskcreateform(forms.ModelForm):
    created =forms.DateField(widget=Datainput)
    class Meta:
        model = TodoTask
        fields=('title','created','category')