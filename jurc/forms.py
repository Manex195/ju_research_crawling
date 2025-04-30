from django import forms

class AuthorSearchForm(forms.Form):
  author_name = forms.CharField(
    label='Search by Author',
    max_length=100,
    widget=forms.TextInput(attrs={'placeholder': 'Enter an author name'})
  )