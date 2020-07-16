from django.forms import ModelForm, TextInput

from .models import Task


class TaskForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = ''

    class Meta:
        model = Task
        fields = ['title']

        widgets = {
            'title': TextInput(attrs={'class': 'rounded form-control', 'id': 'task-input', 'placeholder': 'Enter a task...'})
        }
