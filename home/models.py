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
    title = models.CharField(max_length=150)
    cooking_time = models.IntegerField(default=-1)
    number_of_servings = models.IntegerField(default=1)
    complexity = models.ForeignKey(Complexity, on_delete=models.PROTECT, default=1)
    ingredients = models.TextField(null=False)
    steps = models.TextField(null=False)
    calories = models.FloatField(default=0)
    proteins = models.FloatField(default=0)
    fats = models.FloatField(default=0)
    carbohydrates = models.FloatField(default=0)
    _type = models.ForeignKey(Type, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tags)
    author_name = models.CharField(max_length=150)
    author_link = models.CharField(max_length=150)
    quote = models.TextField()
    preview_photo = models.ImageField(upload_to=path_and_rename)
    views = models.IntegerField(default=0)
    published = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=150, unique=True, null=False, blank=True)
    kitchen = models.ForeignKey(Type_of_kitchen, on_delete=models.PROTECT, default=1)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.url = RuTextToSlug(self.title) + f"_{self.pk}"

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"
