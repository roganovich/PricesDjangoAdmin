from django.core.management.base import BaseCommand
from emailparser import models
import os

class Command(BaseCommand):
    help = 'Import Suppliers data from dir'

    def handle(self, *args, **kwargs):
        path = '../../pythonEmailPriceLoader/parsers'
        # Находим файлы классов разных постащиков
        for dirpath, dirnames, filenames in os.walk(path):
            # перебрать файлы

                for filename in filenames:
                    filename = os.path.join(dirpath, filename)
                    try:
                        print("Файл:", filename)
                        supplier_rows = []
                        # Открываем файл для разбора
                        with open(filename) as file:
                            # Сигнал о начале полехной информации
                            start_get_data = False
                            # Разбираем файл по строкам
                            for line in file:
                                #print(line.rstrip())
                                # Очищаем строки
                                line = line.replace('"', '')
                                line = line.replace(' ', '\t')
                                line = line.replace('\\', '/')
                                line = line.expandtabs(13)
                                line = line.replace(" ", "").rstrip()

                                # Находим строку начала класса
                                find_start_row = line.find("class")
                                if find_start_row != -1:
                                    start_get_data = True

                                # Находим строки где есть назначение свойство
                                rule = line.find("=")

                                # Проверяем параметры строки
                                if(start_get_data == True and line and rule != -1):
                                    # Разбиваем строку на параметры с ключами свойство=значение
                                    supplier_rows.append(line.split("="))

                            # Создаем запись о найденном поставщике
                            if (supplier_rows):
                                self.prepareSupplier(supplier_rows)
                    except:
                        print('Не смог обработать файл: ' + str(filename))
                        continue

    # Функция для создания записи о Поставщике из данных собраных обработкой файлов
    def prepareSupplier(self, supplier_rows):

        supplier_data = {
            'name': '',
            'email_addres': '',
            'email_title': '',
            'suppliers_id': 0,
            'warhouse_id': 0,
            'clearLine': 0,
            'parsertype': '',
            'filetype': '',
            'fileEncoding': '',
            'delimiter': '',
            'colums': '',
        }

        for row in supplier_rows:
            key = row[0]
            val = row[1]
            if(key in supplier_data):
                supplier_data[key] = val

        new_sup = models.Supplier(
            name = supplier_data['name'],
            email_addres=supplier_data['email_addres'],
            email_title=supplier_data['email_title'],
            suppliers_id=supplier_data['suppliers_id'],
            warhouse_id=supplier_data['warhouse_id'],
            clear_line=supplier_data['clearLine'],
            parser_type=supplier_data['parsertype'],
            file_type=supplier_data['filetype'],
            file_encoding=supplier_data['fileEncoding'],
            file_delimiter=supplier_data['delimiter'].replace('/', '\\'),
            colums=supplier_data['colums']
        )

        return new_sup.save()