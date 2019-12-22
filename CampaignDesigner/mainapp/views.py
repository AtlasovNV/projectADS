from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .forms import KeyWordsForm, FastLinkAndOther
from .models import Campaign, Frases, SharedDataGroup, FastLink, Regions
from django.views.generic import CreateView
import xlsxwriter


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
            verfeinerungen_1 = form.cleaned_data['verfeinerungen_1']
            header_fast_link_2 = form.cleaned_data['header_fast_link_2']
            text_fast_link_2 = form.cleaned_data['text_fast_link_2']
            link_fast_link_2 = form.cleaned_data['link_fast_link_2']
            verfeinerungen_2 = form.cleaned_data['verfeinerungen_2']
            header_fast_link_3 = form.cleaned_data['header_fast_link_3']
            text_fast_link_3 = form.cleaned_data['text_fast_link_3']
            link_fast_link_3 = form.cleaned_data['link_fast_link_3']
            verfeinerungen_3 = form.cleaned_data['verfeinerungen_3']
            header_fast_link_4 = form.cleaned_data['header_fast_link_4']
            text_fast_link_4 = form.cleaned_data['text_fast_link_4']
            link_fast_link_4 = form.cleaned_data['link_fast_link_4']
            verfeinerungen_4 = form.cleaned_data['verfeinerungen_4']
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
            new_fast_link.verfeinerungen_1 = verfeinerungen_1
            new_fast_link.verfeinerungen_2 = verfeinerungen_2
            new_fast_link.verfeinerungen_3 = verfeinerungen_3
            new_fast_link.verfeinerungen_4 = verfeinerungen_4
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
    workbook = xlsxwriter.Workbook(f'Рекламная кампания Яндекс Директ_{pk}.xlsx')
    worksheet = workbook.add_worksheet()

    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': True})

    # Write some data headers.
    worksheet.write('A1', 'Доп. объявление группы', bold)
    worksheet.write('B1', 'Назвиние группы', bold)
    worksheet.write('C1', 'Фраза (с минус-словами)', bold)
    worksheet.write('D1', 'Заголовок 1', bold)
    worksheet.write('E1', 'Заголовок 2', bold)
    worksheet.write('F1', 'Текст', bold)
    worksheet.write('G1', 'Ссылка', bold)
    worksheet.write('I1', 'Отображаемая ссылка', bold)
    worksheet.write('H1', 'Ставка', bold)
    worksheet.write('J1', 'Регион', bold)
    worksheet.write('K1', 'Заголовки быстрых ссылок', bold)
    worksheet.write('L1', 'Описания быстрых ссылок', bold)
    worksheet.write('M1', 'Адреса быстрых ссылок', bold)
    worksheet.write('N1', 'Уточнения', bold)

    frases = Frases.objects.filter(campaign__pk=pk)

    row = 1

    for frase in frases:
        expenses = (
            [
                frase.additional_ad,
                frase.name_group.name_group,
                frase.frase,
                frase.headers.header1,
                frase.headers.header2,
                frase.shared_data_group.text,
                frase.shared_data_group.link,
                frase.shared_data_group.bewerten,
                frase.shared_data_group.sangezeigt_link,
                frase.region.region,
                frase.fast_link.header_fast_link_1 + ' || ' +
                    frase.fast_link.header_fast_link_2 + ' || ' +
                    frase.fast_link.header_fast_link_3 + ' || ' +
                    frase.fast_link.header_fast_link_4,
                frase.fast_link.text_fast_link_1 + ' || ' +
                    frase.fast_link.text_fast_link_2 + ' || ' +
                    frase.fast_link.text_fast_link_3 + ' || ' +
                    frase.fast_link.text_fast_link_4,
                frase.fast_link.link_fast_link_1 + ' || ' +
                     frase.fast_link.link_fast_link_2 + ' || ' +
                     frase.fast_link.link_fast_link_3 + ' || ' +
                     frase.fast_link.link_fast_link_4,
                frase.fast_link.verfeinerungen_1 + ' || ' +
                     frase.fast_link.verfeinerungen_2 + ' || ' +
                     frase.fast_link.verfeinerungen_3 + ' || ' +
                     frase.fast_link.verfeinerungen_4,
                ],
        )
        for minus, namegroup, frase, header1, header2, text, link, linkview, \
            bewerten, region, headerfastlink, textfastlink, linkfastlink, \
            verfeinerungen in (expenses):

            worksheet.write(row, 0, minus)
            worksheet.write(row, 1, namegroup)
            worksheet.write(row, 2, frase)
            worksheet.write(row, 3, header1)
            worksheet.write(row, 4, header2)
            worksheet.write(row, 5, text)
            worksheet.write(row, 6, link)
            worksheet.write(row, 7, linkview)
            worksheet.write(row, 8, bewerten)
            worksheet.write(row, 9, region)
            worksheet.write(row, 10, headerfastlink)
            worksheet.write(row, 11, textfastlink)
            worksheet.write(row, 12, linkfastlink)
            worksheet.write(row, 13, verfeinerungen)
        row += 1

    workbook.close()
