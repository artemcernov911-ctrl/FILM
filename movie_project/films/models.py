from django.db import models

class Films(models.Model):
    name = models.CharField('Название фильма', max_length=200)
    description = models.TextField('Описание фильма')
    review = models.CharField('Отзыв', max_length=200)

    def __str__(self):
        return self.name
