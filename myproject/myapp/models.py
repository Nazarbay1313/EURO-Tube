from django.db import models
from django.urls import reverse
from embed_video.fields import EmbedVideoField

from myproject.settings import AUTH_USER_MODEL

# Create your models here.


class Product(models.Model):
    initiator = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, verbose_name='Автор')
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.SlugField(unique=True, verbose_name='URL')
    content = models.TextField(verbose_name='Описание')
    video = EmbedVideoField(verbose_name='Видео')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления', null=True)
    tags = models.ManyToManyField('Tag', verbose_name='Теги')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')

    class Meta:
        verbose_name = 'Посты'
        verbose_name_plural = 'Посты'
        ordering = ('-id',)

    def __str__(self):
        return f"Пост от {self.initiator}"


class Tag(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название тега')
    slug = models.SlugField(unique=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Теги'
        verbose_name_plural = 'Теги'
        ordering = ('-id',)

    def __str__(self):
        return f"Тег {self.title}"

    def get_absolute_url(self):
        return reverse('tags', kwargs={'tag_slug': self.slug})


class Favorite(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'
        ordering = ('-id',)

    def __str__(self):
        return f'Избранные для {self.user}'


class Comment(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    content = models.TextField(verbose_name='Комментарий')

    class Meta:
        verbose_name = 'Комментарии'
        verbose_name_plural = 'Комментарии'
        ordering = ('-id',)

    def __str__(self):
        return f'Комментарий пользователя {self.user}'
