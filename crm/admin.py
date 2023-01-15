from django.contrib import admin
#импортируем в админ-панель класс Ордер
from .models import Order, StatusCrm, CommentCrm

# Register your models here.


class Comment(admin.StackedInline):
    # Обязательный атрибут - модель, к которой относится данный класс
    model = CommentCrm
    # Поля объекта
    fields = ('comment_dt', 'comment_text')
    readonly_fields = ('comment_dt',)
    # Уменьшение кол-ва показываемых комментов
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    # отображаемые параметры в общем спискe
    list_display = ('id', 'order_status', 'order_name', 'order_phone', 'order_dt')
    # кликабельные параметры в общем списке
    list_display_links = ('id', 'order_name')
    # параметры, по которым можно искать объекты в общем списке
    search_fields = ('id', 'order_name', 'order_phone', 'order_dt')
    # фильтр, по которому можно выбрать объекты в общем списке
    list_filter = ('order_status',)
    # изменяемые параметры объектов в общем списке
    list_editable = ('order_status', 'order_phone')
    # количество объектов на одной странице
    list_per_page = 10
    # максимальное кол-во объектов в общем списке
    list_max_show_all = 100

    # Поля определенного объекта
    fields = ('id', 'order_dt', 'order_status', 'order_name', 'order_phone')
    readonly_fields = ('id', 'order_dt')

    # Поле класса Comment - передаем класс Comment в наш основной класс
    inlines = (Comment,)

# Напрямую добавляем все объекты класса Ордер в админ-панель (регистрируем)


admin.site.register(Order, OrderAdmin)
admin.site.register(StatusCrm)
admin.site.register(CommentCrm)

