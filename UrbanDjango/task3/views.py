from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


def platform(request):
    title = 'Главная страница'
    home = 'Главная'
    shop = 'Магазин'
    cart = 'Корзина'

    context = {'title': title, 'home': home, 'shop': shop, 'cart': cart}
    return render(request, 'platform.html', context)


def games(request):
    title = 'Игры'
    game_action = 'Экшен'
    game_strategy = 'Стратегии'
    game_race = 'Гонки'
    ks = 'Counter Strike 1.6 (КС 1.6)'
    bm = 'Black Myth: Wukong'
    gow = 'God of War Ragnarok'
    ants = 'Empire of the Ants'
    aoe = 'Age of Empires 2 (II) Definitive Edition'
    dune = 'Dune Spice Wars'
    to = 'TRAIL OUT'
    carx = 'CarX Street'
    nfs = 'Need for Speed: Underground 2'

    context = {
        'title': title, 'game_action': game_action, 'game_strategy': game_strategy, 'game_race': game_race,
        'ks': ks, 'bm': bm, "gow": gow, "ants": ants, "aoe": aoe, "dune": dune, 'to': to, "carx": carx, 'nfs': nfs
    }
    return render(request, 'games.html', context)


def cart(request):
    title = 'Корзина'
    text = 'Извините, Ваша корзина пуста'
    context = {'title': title, 'text': text}
    return render(request, 'cart.html', context)
