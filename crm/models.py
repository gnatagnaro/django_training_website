from django.db import models

# Create your models here.



class Order(models.Model):
    '''Класс Ордер наследует моделс и присваивает переданные параметры
    по нужным полям'''
    # verbose_name - для изменения названий атрибутов объектов
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name='Имя')
    order_phone = models.CharField(max_length=200, verbose_name='Телефон')

    #Магический метод меняет изменение отображения объектов
    def __str__(self):
        return self.order_name

    #СубКласс Мета нужен для изменения order и orders
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'