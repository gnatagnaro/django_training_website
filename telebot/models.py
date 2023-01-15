from django.db import models

# Create your models here.


class TeleSettings(models.Model):
    tg_token = models.CharField(max_length=200, verbose_name='Токен')
    tg_chat = models.CharField(max_length=200, verbose_name='Чат id')
    tg_message = models.TextField(verbose_name='Текст сообщения')
    #tg_message_id = models.CharField(max_length=200, verbose_name='ID ')

    '''Изменение отображения имен существующих объектов в списке'''

    def __str__(self):
        return self.tg_chat

    '''Изменение имен, обобщающих список объектов'''

    class Meta:
        verbose_name = 'Настройку'
        verbose_name_plural = 'Настройки'