from django.db import models


class Article(models.Model):
    title = models.CharField('Заголовок', max_length=250)
    content = models.TextField('Текст')
    published_at = models.DateTimeField('Дата публікації')

    

    def __str__(self) -> str:
        return self.title
