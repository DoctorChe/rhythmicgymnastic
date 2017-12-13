from django.shortcuts import render


def index(request):
    return render(request, 'home/home.html')


def contact(request):
    return render(request, 'home/basic.html',
                  {'content':
                       ['If you would like to contact me, please email me.', 'cool.rhythmicgymnastics@yandex.ru']})