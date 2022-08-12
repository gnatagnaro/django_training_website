from django.contrib import admin
#импортируем в админ-панель класс Ордер
from .models import Order

# Register your models here.

#Напрямую добавляем все объекты класса Ордер в админ-панель (регистрируем)
admin.site.register(Order)

