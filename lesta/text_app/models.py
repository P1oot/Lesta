from django.db import models


class File(models.Model):
    file = models.FileField(
        verbose_name='Файл',
        upload_to='files/',
    )
    upload_at = models.DateTimeField(
        verbose_name='Время загрузки',
        auto_now_add=True,
    )
    processed = models.BooleanField(
        verbose_name='Статус загрузки',
        default=False,
    )

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'


class Words(models.Model):
    file = models.ForeignKey(
        File,
        on_delete=models.CASCADE,
        related_name='words',
        verbose_name='Файл',
    )
    word = models.TextField(
        verbose_name='Слово',
        max_length=20,
    )
    quantity = models.IntegerField(
        verbose_name='Число встречь слова',
        default=0,
    )
    tf = models.FloatField(
        verbose_name='Частота слова',
        default=0,
    )

    class Meta:
        verbose_name = 'Слово'
        verbose_name_plural = 'Слова'
