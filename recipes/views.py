from django.shortcuts import render
from .models import Recipe
from django.views import generic

class RecipeView(generic.DetailView):
    model = Recipe
    template_name = 'recipe.html'

class AboutView(generic.TemplateView):
    template_name = 'about.html'

class RecipeList(generic.ListView):
    queryset = Recipe.objects.filter(status=1).order_by('-date_created')
    template_name = 'index.html'