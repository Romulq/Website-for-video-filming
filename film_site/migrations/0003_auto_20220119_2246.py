# Generated by Django 3.2.11 on 2022-01-19 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film_site', '0002_auto_20220119_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата создания заказа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='eventDate',
            field=models.DateField(),
        ),
    ]
