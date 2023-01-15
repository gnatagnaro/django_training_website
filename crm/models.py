'''III - Запрос поступает из views.py. Происходит обмен данными с БД,
происходит обмен значениями из полей - нужное передается во views.py'''
from django.db import models

# Create your models here.


class StatusCrm(models.Model):
    status_name = models.CharField(max_length=200, verbose_name='Название статуса')

    def __str__(self):
        return self.status_name

     #СубКласс Мета нужен для изменения order и orders
    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Order(models.Model):
    '''Класс Ордер наследует моделс и присваивает переданные параметры
    по нужным полям'''
    # verbose_name - для изменения названий атрибутов объектов
    order_dt = models.DateTimeField(auto_now=True, verbose_name='Дата заказа')
    order_name = models.CharField(max_length=200, verbose_name='Имя')
    order_phone = models.CharField(max_length=200, verbose_name='Телефон')
    #null - одобрение пустоты в БД, true - пустота в админ-панели Django
    order_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Статус')

    #Магический метод изменяет отображение объектов
    def __str__(self):
        return self.order_name

    #СубКласс Мета нужен для изменения order и orders
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class CommentCrm(models.Model):
    comment_binding = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заявка')
    comment_text = models.TextField(verbose_name='Текст комментария')
    comment_dt = models.DateTimeField(auto_now=True, verbose_name='Дата комментария')


    # Магический метод изменяет отображение объектов
    def __str__(self):
        return self.comment_text

    # СубКласс Мета нужен для изменения order и orders
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
