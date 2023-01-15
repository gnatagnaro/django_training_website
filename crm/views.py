'''II - генерация страниц с данными в ответ на запрос,
запрос приходит из urls.py, а данные запрашиваются из models.py'''

'''IV - получаем значения полей из классов из models.py, а функцией
render эти же данные передаются в html-шаблон по определенным ссылкам
и ключам'''
from django.shortcuts import render
#импорт класса Ордер из моделс
from .models import Order
from .forms import OrderForm
from cms.models import CmsSlider
from price.models import PriceCard, PriceTable
from telebot.sendmessage import sendTelegram

# Create your views here.

def first_page(request):
    '''Функция рендерит страницу index.html, импортируем в urls'''
    # Переменная, включающая все элементы QuerySet
    slider_list = CmsSlider.objects.all()
    pc_1 = PriceCard.objects.get(pk=1)
    pc_2 = PriceCard.objects.get(pk=2)
    pc_3 = PriceCard.objects.get(pk=3)
    price_table = PriceTable.objects.all()
    form = OrderForm()
    dict_obj = {'slider_list': slider_list, 'price_table': price_table,
                'pc_1': pc_1, 'pc_2': pc_2, 'pc_3': pc_3,
                'form': form}
    return render(request, './index.html', dict_obj)


def thanks_page(request):
    '''Функция рендерит страницу thanks_page.html, импортируем в urls'''
    # В html форме мы получили запрос. Чтобы его распознать, используем:
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']

        # Сохраняем данные в базе данных
        element = Order(order_name=name, order_phone=phone)
        element.save()
        sendTelegram(tg_name=name, tg_phone=phone)

        # Передаем полученные данные из запроса в рендер html-страницы
        return render(request, './thanks.html', {'name': name, 'phone': phone})
    else:
        return render(request, './thanks.html')
