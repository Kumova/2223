from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

DATA = {
    'omlet': {
        'яйца,шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'cheesecakes': {
        'творог, г': 200,
        'яйцо, шт': 1,
        'мука, г': 20,
        'сахар, г': 5,
    }
}


def recipes(request, recipe):
    recipe=request.GET.get("recipe")
    servings = int(request.GET.get("servings", '')
    if recipe:
       recipe=amount*servings
    return HttpResponse(recipe)
 #   else:
 #      return HttpResponse(f'Такого рецепта не знаю')
    context = {
        'recipe': {
            'ingredient': amount,
        }
    }
    return render(request, 'calculator/index.html', context)



