from django.http import HttpResponseRedirect, HttpResponse, request
from django.shortcuts import render
import xlwt
from mainapp.savexls import savelxs
from .forms import KeyWordsForm



def main(request):
    return render(request, 'mainapp/index.html',)


def first_page(request):
    if request.method == 'POST':
        form = KeyWordsForm(request.POST)

        if form.is_valid():
            frase = form.cleaned_data['keywords']
            # new_keywords = keywords.replace(' ', '-')               # замена пробелов на минус
            # s = [s.strip('-') for s in new_keywords.splitlines()]   # создание списка с переносом строки
            # str_list = list(filter(None, s))
            # for i, frase in enumerate(str_list):  # запись ввода пользователя в таблицу
            #     i += 1
            #     print(frase)
            savelxs(frase)
    else:
        form = KeyWordsForm()

    return render(request, 'mainapp/first_page.html', {'form': form})





def second_page(request):
    return render(request, 'mainapp/second_page.html')




