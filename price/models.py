from django.db import models

# Create your models here.


class PriceCard(models.Model):
    '''Изменение имен напротив добавления новых объектов'''
    pc_value = models.CharField(max_length=200, verbose_name='Цена')
    pc_description = models.CharField(max_length=200, verbose_name='Описание')

    '''Изменение отображения имен существующих объектов в списке'''
    def __str__(self):
        return self.pc_value


    '''Изменение имен, обобщающих список объектов'''
    class Meta:
        verbose_name = 'Цену'
        verbose_name_plural = 'Цены'


class PriceTable(models.Model):
    '''Имена напротив вводимых значений новых объектов
    Например:
    Услуга:
    Старая цена:'''
    pt_title = models.CharField(max_length=200, verbose_name='Услуга')
    pt_old_price = models.CharField(max_length=200, verbose_name='Старая цена')
    pt_new_price = models.CharField(max_length=200, verbose_name='Новая цена')

    '''Отображение уникальных имен в общем списке'''
    def __str__(self):
        return self.pt_title

    '''Общее обозначение предметов списка'''
    class Meta:
        verbose_name = 'Услугу'
        verbose_name_plural = 'Услуги'