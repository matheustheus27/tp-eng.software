# Generated by Django 4.2.2 on 2023-07-01 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appPizzaria', '0004_menu_list_drinks_menu_list_pizzas_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='drink',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='pizza',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='promotion',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
