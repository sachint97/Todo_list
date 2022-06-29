from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User, Task


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Email')

    class Meta():
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'complete']

        widgets = {
            'title': forms.TimeInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'complete': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


