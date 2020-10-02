from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver


class Task(models.Model):
    title = models.CharField('Название', max_length=50) # CharField для мелких текстов (<250 символов)
    task = models.TextField('Описание') # TextField для больших текстов (>250 символов)
#    date = models.DateTimeField()
#    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'  # изменение названия таблицы
        verbose_name_plural = 'Задачаи'


# class Comments(models.Model):
#     comments_text = models.TextField
#     comments_task = models.ForeignKey(Task) # Связь между Таском и Коментариями
#
#     class Meta():
#         verbose_name = 'Коментарий'  # изменение названия таблицы
#         verbose_name_plural = 'Коментарии'


#class Profile(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE)
#    bio = models.TextField(max_length=500, blank=True)
#    location = models.CharField(max_length=30, blank=True)
#    birth_date = models.DateField(null=True, blank=True)
