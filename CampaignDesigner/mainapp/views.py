from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from .forms import KeyWordsForm
import xlwt


def main(request):
    return render(request, 'mainapp/index.html',)


def first_page(request):
    form = KeyWordsForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            return HttpResponseRedirect(reverse('main:second_page'))
    else:
        form = KeyWordsForm()
    return render(request, 'mainapp/first_page.html', {'form': form})


def second_page(request):
    if request.method == "POST":
        form = KeyWordsForm(request.POST)
        if form.is_valid():
            keywords = form.cleaned_data['keywords']
            cross_keywords = keywords.replace(' ', '-')
            split_cross_keywords_list = [s.strip('-') for s in cross_keywords.splitlines()]
            split_upper_keywords_list = [s.strip(' ') for s in keywords.splitlines()]

            cross_keywords_list = list(filter(None, split_cross_keywords_list))
            upper_keywords_list = list(filter(None, split_upper_keywords_list))

            upper_keywords = [i.capitalize() for i in upper_keywords_list]

            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('Sheet1')
            columns = ['Фразы с минус словами', ]  # титульные колонки
            row_num = 0
            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num])  # запись титульников в таблицу
            for i, e in enumerate(cross_keywords_list):  # запись ввода пользователя в таблицу
                ws.write(i + 1, 0, e)
            name = "spreadsheet.xls"
            wb.save(name)
    else:
        return HttpResponseRedirect(reverse('main:first_page'))

    context = {"upper_keywords": upper_keywords}

    return render(request, 'mainapp/second_page.html', context)