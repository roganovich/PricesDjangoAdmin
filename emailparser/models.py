from django.db import models
from django.urls import reverse
from django.contrib import admin
from django.shortcuts import redirect

class Supplier(models.Model):
    """
    Model representing a Supplier.
    """

    PARSER_TYPES_CHOICES = [
        ('file', 'file'),
        ('zip', 'zip'),
        ('rar', 'rar')
    ]

    FILE_TYPES_CHOICES = [
        ('csv', 'csv'),
        ('xls', 'xls'),
        ('xlsx', 'xlsx'),
        ('xml', 'xml'),
    ]

    FILE_ENCODING_CHOICES = [
        ('utf-8', 'utf-8'),
        ('windows-1251', 'windows-1251'),
    ]

    FILE_DELIMETERS = [
        ('\\t', 'Табуляция'),
        (';', 'Точка с запятой'),
        (',', 'Запятая'),
    ]

    name = models.CharField(verbose_name="Название", max_length=128, help_text="Укажите название прайса")
    email_addres = models.CharField(verbose_name="Email письма", max_length=64, help_text="Укажите адрес email с которого приходит прайс", null=True, blank=True)
    email_title = models.CharField(verbose_name="Title письма", max_length=64, help_text="Укажите тему письма с которого приходит прайс", null=True, blank=True)
    email_attachment = models.CharField(verbose_name="Вложение письма", max_length=64, help_text="Укажите имя вложения которое приходит в письме", null=True, blank=True)
    suppliers_id = models.IntegerField(verbose_name="ИД Поставщика", help_text="Укажите ИД поставщика в БД")
    warhouse_id = models.IntegerField(verbose_name="ИД Склада", help_text="Укажите ИД склада в Бд, если нужно", null=True, blank=True)
    clear_line = models.IntegerField(verbose_name="Пустых строк",help_text="Количество строк которые нужно пропустить", default=0, blank=True)
    parser_type = models.CharField(verbose_name="Тип вложения", max_length=32, help_text="Тип вложения в письме", choices=PARSER_TYPES_CHOICES)
    file_type = models.CharField(verbose_name="Тип файла", max_length=32, help_text="Тип файла прайса", choices=FILE_TYPES_CHOICES)
    file_encoding = models.CharField(verbose_name="Кодировка файла", max_length=32, help_text="Кодировка файла (Для файлов CSV)", null=True, blank=True, choices=FILE_ENCODING_CHOICES)
    file_delimiter = models.CharField(verbose_name="Разделитель строк", max_length=32, help_text="Разделитель строк (Для файлов CSV)", choices=FILE_DELIMETERS, null=True, blank=True)
    unity = models.TextField(verbose_name="Соотмествия файлов", help_text="Json: Соответствие имени файла со складом", null=True, blank=True)
    colums = models.TextField(verbose_name="Соответствия колонок", help_text="Json: Значение колонок в файле")

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name


    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('supplier-detail', args=[str(self.id)])

# Define the admin class
class SupplierAdmin(admin.ModelAdmin):

    list_display  = ('name', 'email_addres', 'email_title', 'suppliers_id', 'warhouse_id', 'parser_type', 'file_type')
    search_fields = ['name', 'email_addres', 'email_title']

    actions = ['clone']

    @admin.action(description='Клонировать запись')
    def clone(self, request, queryset):
        for obj in queryset:
            new_obj = obj
            new_obj.pk = None
            new_obj.save()
            response = redirect('/admin/emailparser/supplier/' + str(new_obj.id) + '/change')
            return response


