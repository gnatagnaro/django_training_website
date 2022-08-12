from django.shortcuts import render
#импорт класса Ордер из моделс
from .models import Order

from .forms import OrderForm
# Create your views here.

def first_page(request):
    '''Функция рендерит страницу index.html, импортируем в urls'''

    #Переменная, включающая все элементы QuerySet
    object_list = Order.objects.all()
    form = OrderForm()
    return render(request, './index.html', {'object_list': object_list,
                                            'form': form})


def thanks_page(request):
    '''Функция рендерит страницу thanks_page.html, импортируем в urls'''
    #В html форме мы получили запрос. Чтобы его распознать, используем:
    name = request.POST['name']
    phone = request.POST['phone']

    #Сохраняем данные в базе данных
    element = Order(order_name = name, order_phone = phone)
    element.save()

    #Передаем полученные данные из запроса в рендер html-страницы
    return render(request, './thanks_page.html', {'name': name,
                                                  'phone': phone})