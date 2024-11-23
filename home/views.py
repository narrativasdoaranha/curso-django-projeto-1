from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    print('Eu posso fazer o que quiser')
    return render(
    request,
    'home/index.html'
    )

