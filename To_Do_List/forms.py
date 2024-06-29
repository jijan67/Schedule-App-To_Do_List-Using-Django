from django import forms
from .models import TodoList

class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add custom CSS classes to form fields
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['style'] = 'background-color: white; border: 2px solid green; color: green; font-weight: bold;'
