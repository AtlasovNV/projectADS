from django import forms


class KeyWordsForm(forms.Form):
    keywords = forms.CharField(widget=forms.Textarea, max_length=2000)
