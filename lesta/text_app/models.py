from django.db import models


class File(models.Model):
    file = models.FileField(
        verbose_name='Файл',
        upload_to='files/',
    )
    name = models.TextField(
        verbose_name='Название документа',
    )
    upload_at = models.DateTimeField(
        verbose_name='Время загрузки',
        auto_now_add=True,
    )
    processed = models.BooleanField(
        verbose_name='Статус загрузки',
        default=False,
    )
    quantity = models.IntegerField(
        verbose_name='Количество слов',
        null=True,
    )
    words_list = models.TextField(
        verbose_name='50 наиболее частых слов',
    )

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
