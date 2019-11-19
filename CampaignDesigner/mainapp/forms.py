from django import forms
from mainapp.models import Template


class KeyWordsForm(forms.Form):
    keywords = forms.CharField(widget=forms.Textarea, max_length=2000)


class TemplateCreateForm(forms.ModelForm):
    class Meta:
        model = Template
        fields = ('url', 'displayed_url', 'headline_1', 'headline_2', 'text', 'fast_url_1', 'description_1',
                  'fast_url_2', 'description_2', 'fast_url_3', 'description_3', 'fast_url_4', 'description_4',
                  'refinements')
        labels = {
            'url': 'Введите ссылку на сайт',
            'displayed_url': 'Введите отображаемую ссылку',
            'headline_1': 'Введите первый заголовок',
            'headline_2': 'Введите второй заголовок',
            'text': 'Введите текст объявления',
        }



