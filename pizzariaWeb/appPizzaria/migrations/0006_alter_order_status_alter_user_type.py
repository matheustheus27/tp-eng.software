# Generated by Django 4.2.2 on 2023-07-01 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appPizzaria', '0005_drink_price_pizza_price_promotion_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(1, 'Pendente'), (2, 'Aceito'), (3, 'Recusado'), (4, 'Em Preparação'), (5, 'Em Rota'), (6, 'Entregue'), (7, 'Devolvido')], default=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.IntegerField(choices=[(1, 'Cliente'), (2, 'Funcionario')], default=1),
        ),
    ]