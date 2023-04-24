from django import forms

class TodoListForm(forms.Form):
    text = forms.CharField(max_length=45,
                           widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Add a todo item', 'aria-label': 'Example text with button addon', 'aria-describedby': 'button-addon1'}
                           ))