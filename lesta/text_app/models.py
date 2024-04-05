from django.db import models


class File(models.Model):
    file = models.FileField(
        verbose_name='Файл',
        upload_to='files/',
    )
    uplode_at = models.DateTimeField(
        verbose_name='Время загрузки',
        auto_now_add=True,
    )
    processed = models.BooleanField(
        verbose_name='Статус загрузки',
        default=False,
    )

    class Meta:
        verbose_name = 'Файл'
        verbose_name_pural = 'Файлы'


class Words(models.Model):
    word = models.TextField(
        verbose_name='Слово',
        max_length=20,
    )
    tf = models.IntegerField(
        verbose_name='Частота слова',
        default=0,
    )
