from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import CmsSlider


class CmsAdmin(admin.ModelAdmin):

    # Отображение параметров в списке
    list_display = ('cms_title', 'cms_text', 'cms_css', 'get_img', 'cms_img')
    # Кликабельные параметры в списке
    list_display_links = ('cms_title',)
    # Изменяемые параметры в списке
    list_editable = ('cms_css',)
    # Отображение полей объектов
    fields = ('cms_title', 'cms_text', 'cms_css', 'cms_img', 'get_img')
    # Поле только для чтения
    readonly_fields = ('get_img',)

    # Метод для получения изображения объекта
    def get_img(self, obj):
        if obj.cms_img:
            return mark_safe(f'<img src="{obj.cms_img.url}" width="80px">')
        else:
            return 'нет картинки'

    get_img.short_description = 'Миниатюра'

# Register your models here.


admin.site.register(CmsSlider, CmsAdmin)
