import os

from django.db import models

from .Logic import RuTextToSlug, path_and_rename


class Type_of_kitchen(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тип кунхни"
        verbose_name_plural = "Типы кухни"


class Tags(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


# Create your models here.
class Complexity(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Уровень сложности готовки"
        verbose_name_plural = "Уровни сложности готовки"


class Type(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тип блюда"
        verbose_name_plural = "Типы блюд"


class Recipe(models.Model):
    title = models.CharField(max_length=150, help_text='Название блюда')
    cooking_time = models.IntegerField(default=-1, help_text="Время готовки")
    number_of_servings = models.IntegerField(default=1, help_text="Сколько порций")
    complexity = models.ForeignKey(Complexity, on_delete=models.PROTECT, default=1, help_text="Сложность готовки")
    ingredients = models.TextField(null=False, help_text="Ингридиенты")
    steps = models.TextField(null=False, help_text="Шаги приготовления блюда")
    calories = models.FloatField(default=0, help_text="Кол-во калорий на 100гр")
    proteins = models.FloatField(default=0, help_text="Кол-во белков на 100гр")
    fats = models.FloatField(default=0, help_text="Кол-во жиров на 100гр")
    carbohydrates = models.FloatField(default=0, help_text="Кол-во углеводов на 100гр")
    _type = models.ForeignKey(Type, on_delete=models.PROTECT, help_text="Тип блюда")
    tags = models.ManyToManyField(Tags, help_text="Теги")
    author_name = models.CharField(max_length=150, help_text="Имя автора (или сайта)")
    author_link = models.CharField(max_length=150, help_text="ссылка на автора или на сайт")
    quote = models.TextField(help_text="Небольшое описание")
    preview_photo = models.ImageField(upload_to=path_and_rename, help_text="фотка")
    views = models.IntegerField(default=0, help_text="не трогай")
    published = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=150, unique=True, null=False, blank=True, help_text="пиши тут что хочешь")
    kitchen = models.ForeignKey(Type_of_kitchen, on_delete=models.PROTECT, default=1)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.url = RuTextToSlug(self.title) + f"_{self.pk}"

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"
