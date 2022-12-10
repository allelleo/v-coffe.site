from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from v_coffe.settings import MEDIA_URL
from .models import Recipe


# Create your views here.
def index(request):
    context = {
        'title': "Главная страница",
        'menu': [
            {'title': 'Home', 'link': 'home_home', 'active': True},
            {'title': 'About', 'link': 'about', 'active': False},
            {'title': 'New Recipe', 'link': 'new_recipe', 'active': False},
            {'title': 'Contact', 'link': 'contact', 'active': False},
        ]

    }
    return render(request, "home/home.html", context=context)


def about(request):
    return HttpResponse("about")


def new_recipe(request):
    return HttpResponse("new recipe")


def contact(request):
    return HttpResponse("contact")


class AllRecipes(View):
    template_name = 'home/AllRecipes.html'

    def get_context_data(self, **kwargs):
        AllRecipesObjects = Recipe.objects.all()
        return {
            'title': 'Все рецепты',
            'media': MEDIA_URL,
            'recipes': AllRecipesObjects
        }

    def get(self, request):
        return render(request, self.template_name, self.get_context_data())


class GetRecipe(View):
    template_name = 'home/GetRecipe.html'

    def get_context_data(self, recipe, **kwargs):
        CurrentRecipe = Recipe.objects.get(url=recipe)
        CurrentRecipe.views += 1
        CurrentRecipe.save()
        steps = []
        StepNumber = 1
        for step in CurrentRecipe.steps.split("\n"):
            steps.append({'step': step, 'num': StepNumber})
            StepNumber += 1
        return {
            'title': f'Рецепт : {CurrentRecipe.title}',
            'media': MEDIA_URL,
            'recipe': CurrentRecipe,
            'ingredients': CurrentRecipe.ingredients.split("\n"),
            'steps': steps,
            'type': CurrentRecipe._type
        }

    def get(self, request, recipe):
        return render(request, self.template_name, self.get_context_data(recipe))
