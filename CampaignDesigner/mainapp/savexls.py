import xlsxwriter

# Create a workbook and add a worksheet.


def savelxs(frase):
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
    worksheet.write('K1', 'Уточнения', bold)

    plus = '+'
    minus = '-'

    #namegroup = 'namegroup'             # название группы он же ключ указывает юзер
    #frase = 'frase'                     # фраза она же заголовок и название группы указывает функция
    header1 = 'header1'                 # заголов 1 он же ключ и название группы указывает функция
    header2 = 'header2'                 # заголов 2 он же часть заголовка 1, если больше 35 символов или указанный юзер
    text = 'text'                       # текст объявления указывает юзер
    link = 'link'                       # основная ссылка указывает юзер
    sangezeigtlink = 'sangezeigtlink'   # отображаемая ссылка указывает юзер
    bewerten = 'bewerten'               # ставка указывает юзер
    region = 'region'                   # регион указывает юзер
    headerfastlink = 'headerfastlink'   # 4 заголовка быстрых ссылок указывает юзер
    textfastlink = 'textfastlink'       # 4 текст быстрых ссылок указывает юзер
    linkfastkink = 'linkfastkink'       # 4 ссылки быстрых ссылок указывает юзер
    verfeinerungen = 'verfeinerungen'   # 4 уточнения указывает юзер


    # Some data we want to write to the worksheet.
    expenses = (
        [minus, plus, frase],
    )

    # Start from the first cell below the headers.
    row = 1
    col = 0

    # Iterate over the data and write it out row by row.
    for minus, plus, frase in (expenses):

        worksheet.write(row, col, minus)    #записывает минус через строчку
        worksheet.write(row + 1, col, plus) #записывает плюс через строчку
        #worksheet.write(row, col + 1, namegroup) #запись без пропусков столбца
        worksheet.write(row, col + 2, frase)

        # worksheet.write(row, col + 3, header1)
        # worksheet.write(row, col + 4, header2)
        # worksheet.write(row, col + 5, text)
        # worksheet.write(row, col + 6, link)
        # worksheet.write(row, col + 7, sangezeigtlink)
        # worksheet.write(row, col + 8, bewerten)
        # worksheet.write(row, col + 9, region)
        # worksheet.write(row, col + 10, headerfastlink)
        # worksheet.write(row, col + 11, textfastlink)
        # worksheet.write(row, col + 12, linkfastkink)
        row += 1                            #запись без пропусков строки


    workbook.close()

    return

