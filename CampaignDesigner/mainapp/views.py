from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from mainapp.savexls import savelxs
from .forms import KeyWordsForm



def main(request):
    return render(request, 'mainapp/index.html',)


def first_page(request):
    form = KeyWordsForm(request.POST)

    return render(request, 'mainapp/first_page.html', {'form': form})


def headingediting(request):
    frase = KeyWordsForm(request.POST)

    '''Считаем количество символов в заголовках. Если больше 35, то переносим во второй заголовок часть ключей, если мсеньше оставляем'''

    
    return render(request, 'mainapp/headingediting.html', {'form': frase})


def second_page(request):
    return render(request, 'mainapp/second_page.html')




