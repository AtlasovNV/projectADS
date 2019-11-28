from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import KeyWordsForm
from django.views.generic import CreateView, UpdateView
from django.views import generic
from mainapp.models import Template
from mainapp.forms import TemplateCreateForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
import xlwt


def main(request):
    return render(request, 'mainapp/index.html',)


def first_page(request):
    if request.method == 'POST':
        form = KeyWordsForm(request.POST)
        if form.is_valid():
            keywords = form.cleaned_data['keywords']
            new_keywords = keywords.replace(' ', '-')               # замена пробелов на минус
            s = [s.strip('-') for s in new_keywords.splitlines()]   # создание списка с переносом строки
            str_list = list(filter(None, s))                        # удаление пустых элементов из списка

            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('Sheet1')
            columns = ['Фразы с минус словами', ]                   # титульные колонки
            row_num = 0
            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num])        # запись титульников в таблицу
            for i, e in enumerate(str_list):                        # запись ввода пользователя в таблицу
                ws.write(i+1, 0, e)
            name = "spreadsheet.xls"
            wb.save(name)
    else:
        form = KeyWordsForm()

    return render(request, 'mainapp/first_page.html', {'form': form})


class TemplateCreateView(CreateView):
    """Создание нового шаблона"""
    model = Template
    form_class = TemplateCreateForm
    template_name = 'mainapp/second_page.html'
    success_url = reverse_lazy('main:second_page')

    # @method_decorator(user_passes_test(lambda x: x.is_superuser))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(TemplateCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Создание шаблона'
        return context

