
from django import forms
from task.models import Task


class TaskForm (forms.ModelForm):
   class Meta:
        model = Task
        fields = ("nombre","descripcion","realizada")

"""
class TaskForm (forms.Form):
    nombre = forms.CharField(label="Nombre ",max_length=200)
    descripcion = forms.CharField(label="Descripcion ", widget=forms.Textarea)
    realizada = forms.BooleanField(label="Realizada ",required=False)
"""