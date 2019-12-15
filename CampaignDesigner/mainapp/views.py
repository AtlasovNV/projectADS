from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .forms import KeyWordsForm
from .models import Campaign, Frases
from django.views.generic import CreateView
from mainapp.models import Template
from mainapp.forms import TemplateCreateForm
from django.urls import reverse_lazy
import xlwt


def main(request):
    return render(request, 'mainapp/index.html',)


# создаем кампанию в базе после нажатия на кнопку "создать РК" на главной
def campaign_create(request):
    new_campaign = Campaign(user=request.user)
    new_campaign.save()
    # перенаправляем на первую страницу и передаем id кампании
    return HttpResponseRedirect(reverse('mainapp:first_page',
                                        args=[new_campaign.id]))


def first_page(request, pk):
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

            # получаем по id кампанию из бд
            campaign = get_object_or_404(Campaign, pk=pk)
            # и записываем фразы в бд
            for keyword in negative_keywords:
                new_frase = Frases(campaign=campaign)
                new_frase.frase = keyword
                new_frase.save()
            print('3')
            return HttpResponseRedirect(reverse('mainapp:second_page', args=[pk]))
    else:
        form = KeyWordsForm()
    content = {
        'form': form,
        'pk': pk,
    }
    return render(request, 'mainapp/first_page.html', content)


def second_page(request, pk):
    return render(request, 'mainapp/second_page.html')


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


def fourth_page(request, pk):
    pass
