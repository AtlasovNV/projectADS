from django import forms
from mainapp.models import Template


class KeyWordsForm(forms.Form):
    keywords = forms.CharField(widget=forms.Textarea, max_length=2000)


class TemplateEditForm(forms.ModelForm):
    class Meta:
        model = Template
        fields = ('url', 'displayed_url', 'headline_1', 'headline_2', 'text',)
        labels = {
            'url': 'Введите ссылку на сайт',
            'description': 'Введите отображаемую ссылку',
            'sort': 'Введите первый заголовок',
            'is_active': 'Введите второй заголовок',
            'shelter_logo': 'Введите текст объявления',
        }
