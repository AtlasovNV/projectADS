import mimetypes
import os

from django.forms import modelformset_factory
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import get_object_or_404

from .titles import title_slice
from .savexls import savexls
from .forms import KeyWordsForm, FastLinkAndOther
from .models import Campaign, Frases, SharedDataGroup, FastLink, Regions, \
    Header, GroupName


def main(request):
    return render(request, 'mainapp/index.html', )


# создаем кампанию в базе после нажатия на кнопку "создать РК" на главной
def campaign_create(request):
    if request.user.is_authenticated:
        new_campaign = Campaign(user=request.user)
        new_campaign.save()
        # перенаправляем на первую страницу и передаем id кампании
        return HttpResponseRedirect(reverse('mainapp:first_page',
                                            args=[new_campaign.id]))
    return HttpResponseRedirect(reverse('auth:login'))


def first_page(request, pk):
    if request.method == "POST":
        form = KeyWordsForm(request.POST)
        if form.is_valid():
            keywords_str = form.cleaned_data['keywords']
            uncommon_keywords = []
            negative_keywords = []
            keywords_list = keywords_str.split()
            keywords_split = [keyword.strip() for keyword in
                              keywords_str.splitlines()]

            keywords_split = list(filter(None,
                                         keywords_split))  # список ключевых слов по строчкам
            keywords_list = list(
                filter(None, keywords_list))  # список слов из ключевых слов

            for keyword in keywords_list:
                if keyword not in uncommon_keywords:
                    uncommon_keywords.append(keyword)

            for keyword in keywords_split:
                negative_keywords.append("{} {}".format(keyword, " ".join(
                    "-" + j for j in uncommon_keywords if
                    j.lower() not in keyword.lower())))

            # получаем по id кампанию из бд
            campaign = get_object_or_404(Campaign, pk=pk)
            # и записываем фразы в бд
            for keyword in negative_keywords:
                new_frase = Frases(campaign=campaign)
                new_frase.frase = keyword

                new_group_name = GroupName()
                new_group_name.name_group = keyword
                new_group_name.save()

                new_frase.name_group_id = new_group_name.id
                new_frase.save()

            headers_list = []
            for keyword in keywords_split:
                headers_list.append(title_slice(keyword))

            second_headers = [header[1] for header in headers_list]
            max_second_header = max(second_headers, key=len)

            frases = Frases.objects.filter(campaign__pk=pk)

            for headers, frase in zip(headers_list,
                                      frases):  # Запись заголовков в базу
                header_row = Header()
                if headers[1] != '-':
                    header_row.header1 = headers[0]
                    header_row.header2 = headers[1]
                    header_row.save()
                    frase.headers_id = header_row.id
                    frase.save()
                else:
                    header_row.header1 = headers[0]
                    header_row.header2 = max_second_header
                    header_row.save()
                    frase.headers_id = header_row.id
                    frase.save()

            return HttpResponseRedirect(
                reverse('mainapp:second_page', args=[pk]))
    else:
        form = KeyWordsForm()
    content = {
        'form': form,
        'pk': pk,
    }
    return render(request, 'mainapp/first_page.html', content)


def second_page(request, pk):
    HeaderFormSet = modelformset_factory(Header,
                                         fields=('header1', 'header2'),
                                         extra=0)
    if request.method == 'POST':
        formset = HeaderFormSet(request.POST,
                        queryset=Header.objects.filter(frases__campaign_id=pk))
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect(
                reverse('mainapp:third_page', args=[pk]))
    else:
        formset = HeaderFormSet(queryset=Header.objects.filter(frases__campaign_id=pk))
    content = {
        'pk': pk,
        'formset': formset,
    }
    return render(request, 'mainapp/second_page.html', content)


def third_page(request, pk):
    if request.method == "POST":
        form = FastLinkAndOther(request.POST)
        if form.is_valid():
            link = form.cleaned_data['link']
            sangezeigt_link = form.cleaned_data['sangezeigt_link']
            text = form.cleaned_data['text']
            header_fast_link_1 = form.cleaned_data['header_fast_link_1']
            text_fast_link_1 = form.cleaned_data['text_fast_link_1']
            link_fast_link_1 = form.cleaned_data['link_fast_link_1']
            # verfeinerungen_1 = form.cleaned_data['verfeinerungen_1']
            header_fast_link_2 = form.cleaned_data['header_fast_link_2']
            text_fast_link_2 = form.cleaned_data['text_fast_link_2']
            link_fast_link_2 = form.cleaned_data['link_fast_link_2']
            # verfeinerungen_2 = form.cleaned_data['verfeinerungen_2']
            header_fast_link_3 = form.cleaned_data['header_fast_link_3']
            text_fast_link_3 = form.cleaned_data['text_fast_link_3']
            link_fast_link_3 = form.cleaned_data['link_fast_link_3']
            # verfeinerungen_3 = form.cleaned_data['verfeinerungen_3']
            header_fast_link_4 = form.cleaned_data['header_fast_link_4']
            text_fast_link_4 = form.cleaned_data['text_fast_link_4']
            link_fast_link_4 = form.cleaned_data['link_fast_link_4']
            # verfeinerungen_4 = form.cleaned_data['verfeinerungen_4']
            region = form.cleaned_data['region']
            bewerten = form.cleaned_data['bewerten']

            new_link = SharedDataGroup()
            new_link.link = link
            new_link.sangezeigt_link = sangezeigt_link
            new_link.text = text
            new_link.bewerten = bewerten
            new_link.save()

            new_fast_link = FastLink()
            new_fast_link.header_fast_link_1 = header_fast_link_1
            new_fast_link.header_fast_link_2 = header_fast_link_2
            new_fast_link.header_fast_link_3 = header_fast_link_3
            new_fast_link.header_fast_link_4 = header_fast_link_4
            new_fast_link.text_fast_link_1 = text_fast_link_1
            new_fast_link.text_fast_link_2 = text_fast_link_2
            new_fast_link.text_fast_link_3 = text_fast_link_3
            new_fast_link.text_fast_link_4 = text_fast_link_4
            new_fast_link.link_fast_link_1 = link_fast_link_1
            new_fast_link.link_fast_link_2 = link_fast_link_2
            new_fast_link.link_fast_link_3 = link_fast_link_3
            new_fast_link.link_fast_link_4 = link_fast_link_4
            new_fast_link.save()

            new_region = Regions()
            new_region.region = region
            new_region.save()

            frases = Frases.objects.filter(campaign__pk=pk)
            for frase in frases:
                frase.shared_data_group_id = new_link.id
                frase.fast_link_id = new_fast_link.id
                frase.region_id = new_region.id
                frase.save()

            return HttpResponseRedirect(
                reverse('mainapp:fourth_page', args=[pk]))
    else:
        form = FastLinkAndOther()
    content = {
        'form': form,
        'pk': pk,
    }
    return render(request, 'mainapp/third_page.html', content)


def fourth_page(request, pk):
    return render(request, 'mainapp/fourth_page.html', {'pk': pk})


def download_xls(request, pk):
    savexls(pk)
    fp = open(f'static/campaign/Рекламная кампания Яндекс Директ_{pk}.xlsx',
              "rb")
    response = HttpResponse(fp.read())
    fp.close()
    file_type = mimetypes.guess_type(
        f'static/campaign/Рекламная кампания Яндекс Директ_{pk}.xlsx')
    if file_type is None:
        file_type = 'application/octet-stream'
    response['Content-Type'] = file_type
    response['Content-Length'] = str(os.stat(
        f'static/campaign/Рекламная кампания Яндекс Директ_{pk}.xlsx').st_size)
    response['Content-Disposition'] = "attachment; filename=rk.xls"

    return response
