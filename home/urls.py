from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import index, about, new_recipe, contact, AllRecipes, GetRecipe

urlpatterns = [
    path("", index, name="home"),
    path("home/", index, name="home_home"),
    path("about/", about, name="about"),
    path("new_recipe/", new_recipe, name="new_recipe"),
    path("contact/", contact, name="contact"),
    path("all-recipes/", AllRecipes.as_view(), name="all_recipes"),
    path("recipe/<slug:recipe>", GetRecipe.as_view(), name="get_recipe"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)