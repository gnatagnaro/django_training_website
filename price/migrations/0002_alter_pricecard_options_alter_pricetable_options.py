# Generated by Django 4.1 on 2022-08-15 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pricecard',
            options={'verbose_name': 'Цену', 'verbose_name_plural': 'Цены'},
        ),
        migrations.AlterModelOptions(
            name='pricetable',
            options={'verbose_name': 'Услугу', 'verbose_name_plural': 'Услуги'},
        ),
    ]
