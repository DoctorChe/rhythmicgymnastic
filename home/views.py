from django.shortcuts import render


def index(request):
    return render(request, 'home/home.html')


def contact(request):
    return render(request, 'home/basic.html',
                  {'content':
                        ['Все свои пожелания Вы можете отправлять на наш почтовый адрес:',
                         'cool.rhythmicgymnastics@yandex.ru']
                   })
