from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

DATA = {
    'omlet': {
        'яйца, шт': 2,
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

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
 #   context = {
#        'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
def recipes(request):
    recipe_name = 'index.html'
    context = {
        'recipe': DATA
    }

    return render(request, 'calculator/index.html', context)

#def calculator(request, количество1, количество2):
#    calculator_name='calculator/index.html'
 #   render(request, 'calculator/index.html', context)
