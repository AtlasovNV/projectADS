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
            keywords_str = form.cleaned_data['keywords']
            uncommon_keywords = []
            negative_keywords = []
            keywords_list = keywords_str.split()
            keywords_split = [keyword.strip() for keyword in keywords_str.splitlines()]

            keywords_split = list(filter(None, keywords_split))             # список ключевых слов по строчкам
            keywords_list = list(filter(None, keywords_list))               # список слов из ключевых слов
            upper_keywords = [keyword.capitalize() for keyword in keywords_split]

            for keyword in keywords_list:
                if keyword not in uncommon_keywords:
                    uncommon_keywords.append(keyword)

            for keyword in keywords_split:
                negative_keywords.append("{} {}".format(keyword, " ".join("-" + j for j in uncommon_keywords if j.lower() not in keyword.lower())))

            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('Sheet1')
            columns = ['Фразы с минус словами', ]                           # титульные колонки
            row_num = 0
            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num])                # запись титульников в таблицу
            for i, e in enumerate(negative_keywords):                       # запись минус слов в таблицу
                ws.write(i + 1, 0, e)
            name = "spreadsheet.xls"
            wb.save(name)
    else:
        return HttpResponseRedirect(reverse('main:first_page'))

    context = {
        "upper_keywords": upper_keywords,
    }

    return render(request, 'mainapp/second_page.html', context)
