from . import views
from django.urls import path

urlpatterns = [
    path('<slug:slug>', views.RecipeView.as_view(), name='recipe_view'),
    path('about/', views.AboutView.as_view(), name='about_view'),
    path('', views.RecipeList.as_view(), name='home'),
]