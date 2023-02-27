from django.db import models

class Task(models.Model):
    title=models.CharField('Заголовок', max_length=50)
    task= models.TextField('Описание')
    prise= models.IntegerField('Сроки')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Задача"
        verbose_name_plural='Задачи'

class Profile(models.Model):
    about_me=models.TextField('О себе:')
    contact=models.TextField('Контактная информация:')

    class Meta:
        verbose_name="Профиль"
        verbose_name_plural="Профили"