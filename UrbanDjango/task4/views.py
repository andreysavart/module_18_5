from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


def platform(request):
     return render(request, 'platform.html')


def games(request):
    title = 'Игры'
    games = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay2']

    context = {
        'title': title, 'games': games}
    return render(request, 'games.html', context)


def cart(request):
    title = 'Корзина'
    text = 'Извините, Ваша корзина пуста'
    context = {'title': title, 'text': text}
    return render(request, 'cart.html', context)
