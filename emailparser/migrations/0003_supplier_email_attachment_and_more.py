# Generated by Django 4.1 on 2022-08-26 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emailparser', '0002_alter_supplier_clear_line_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='email_attachment',
            field=models.CharField(blank=True, help_text='Укажите имя вложения которое приходит в письме', max_length=64, null=True, verbose_name='Вложение письма'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='email_addres',
            field=models.CharField(blank=True, help_text='Укажите адрес email с которого приходит прайс', max_length=64, null=True, verbose_name='Email письма'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='email_title',
            field=models.CharField(blank=True, help_text='Укажите тему письма с которого приходит прайс', max_length=64, null=True, verbose_name='Title письма'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='file_delimiter',
            field=models.CharField(blank=True, choices=[('\\t', 'Табуляция'), (';', 'Точка с запятой'), (',', 'Запятая')], help_text='Разделитель строк (Для файлов CSV)', max_length=32, null=True, verbose_name='Разделитель строк'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='unity',
            field=models.TextField(blank=True, help_text='Json: Соответствие имени файла со складом', null=True, verbose_name='Соотмествия файлов'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='warhouse_id',
            field=models.IntegerField(blank=True, help_text='Укажите ИД склада в Бд, если нужно', null=True, verbose_name='ИД Склада'),
        ),
    ]
