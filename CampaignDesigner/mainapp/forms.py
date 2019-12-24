from django import forms


class KeyWordsForm(forms.Form):
    keywords = forms.CharField(widget=forms.Textarea, max_length=2000)


class FastLinkAndOther(forms.Form):
    link = forms.URLField(label='Введите ссылку на сайт', max_length=200)
    sangezeigt_link = forms.CharField(label='Введите отоброжаемый текст ссылки', max_length=20)
    text = forms.CharField(label='Введите текст объявления', max_length=100)
    header_fast_link_1 = forms.CharField(label='Введите заголовок быстрой ссылки №1', max_length=30)
    text_fast_link_1 = forms.CharField(label='Введите текст быстрой ссылки №1', max_length=60)
    link_fast_link_1 = forms.URLField(label='Введите адрес быстрой ссылки №1', max_length=200)
    verfeinerungen_1 = forms.CharField(label='Введите описание быстрой ссылки №1', max_length=25)
    header_fast_link_2 = forms.CharField(label='Введите заголовок быстрой ссылки №2', max_length=30)
    text_fast_link_2 = forms.CharField(label='Введите текст быстрой ссылки №2', max_length=60)
    link_fast_link_2 = forms.URLField(label='Введите адрес быстрой ссылки №2', max_length=200)
    verfeinerungen_2 = forms.CharField(label='Введите описание быстрой ссылки №2', max_length=25)
    header_fast_link_3 = forms.CharField(label='Введите заголовок быстрой ссылки №3', max_length=30)
    text_fast_link_3 = forms.CharField(label='Введите текст быстрой ссылки №3', max_length=60)
    link_fast_link_3 = forms.URLField(label='Введите адрес быстрой ссылки №3', max_length=200)
    verfeinerungen_3 = forms.CharField(label='Введите описание быстрой ссылки №3', max_length=25)
    header_fast_link_4 = forms.CharField(label='Введите заголовок быстрой ссылки №4', max_length=30)
    text_fast_link_4 = forms.CharField(label='Введите текст быстрой ссылки №4', max_length=60)
    link_fast_link_4 = forms.URLField(label='Введите адрес быстрой ссылки №4', max_length=200)
    verfeinerungen_4 = forms.CharField(label='Введите описание быстрой ссылки №4', max_length=25)
    region = forms.CharField(max_length=50)
    bewerten = forms.DecimalField(max_digits=6, decimal_places=2)
