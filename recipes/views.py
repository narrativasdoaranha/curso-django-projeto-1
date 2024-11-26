from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def recipes(request):
    return render(
    request,
    'recipes/pages/home.html'
    )

def recipes_view(request, id):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Luiz Otávio',
    })

