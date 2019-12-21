import xlsxwriter
from .models import Frases
frases = Frases.objects.filter(campaign__pk=1)


def savexls(self):
    workbook = xlsxwriter.Workbook('Рекламная кампания Яндекс Директ.xlsx')
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
                frase.fast_link.header_fast_link_1 + '||' +
                frase.fast_link.header_fast_link_2 + '||' +
                frase.fast_link.header_fast_link_3 + '||' +
                frase.fast_link.header_fast_link_4,
                frase.fast_link.text_fast_link_1 + '||' +
                frase.fast_link.text_fast_link_2 + '||' +
                frase.fast_link.text_fast_link_3 + '||' +
                frase.fast_link.text_fast_link_4,
                frase.fast_link.link_fast_link_1 + '||' +
                frase.fast_link.link_fast_link_2 + '||' +
                frase.fast_link.link_fast_link_3 + '||' +
                frase.fast_link.link_fast_link_4,
                frase.fast_link.verfeinerungen_1 + '||' +
                frase.fast_link.verfeinerungen_2 + '||' +
                frase.fast_link.verfeinerungen_3 + '||' +
                frase.fast_link.verfeinerungen_4,
            ],
        )

    # start from the first cell below the headers.
        for minus, namegroup, frase, header1, header2, text, link, linkview, \
            bewerten, region, headerfastlink, textfastlink, linkfastlink, \
            verfeinerungen in expenses:
            worksheet.write(row, 5, text)
            for i in range(2):
                if i == 1:
                    worksheet.write(row, 0, '+')
                else:
                    worksheet.write(row, 0, minus)
                worksheet.write(row, 1, namegroup)
                worksheet.write(row, 2, frase)
                worksheet.write(row, 3, header1)
                worksheet.write(row, 4, header2)
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
    return
