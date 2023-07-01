from django.db import models
from enum import Enum

## User
class UserType(Enum):
    COMMON = 1
    MANAGER = 2

class User(models.Model):
    cpf = models.CharField(max_length=11)
    name = models.CharField(max_length=50)
    date_birth = models.DateField()
    type = models.IntegerField(default=1)
    email = models.EmailField()
    phone = models.CharField(max_length=14)
    address = models.CharField(max_length=125)

    def __str__(self):
        return self.name
    
## Menu
class Pizza(models.Model):
    flavor = models.CharField(max_length=50)
    size = models.CharField(max_length=3)
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.flavor
    
class Drink(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    size = models.CharField(max_length=8)

    def __str__(self):
        return self.name
    
class Promotion(models.Model):
    pizza = models.ForeignKey('Pizza', on_delete=models.CASCADE, default=None)
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.id

class Menu(models.Model):
    list_pizzas = models.ManyToManyField(Pizza)
    list_drinks = models.ManyToManyField(Drink)
    list_promotions = models.ManyToManyField(Promotion)

    def __str__(self):
        return "Menu"

## Order
class OrderStatus(Enum):
    PENDING: 1
    APPROVED: 2
    REPROVED: 3
    IN_PREPARATION: 4
    AT_DELIVERY_ROUTE: 5
    DELIVERED: 6
    RETURNED: 7

class Item(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, null=True, default=None)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE, null=True, default=None)
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE, null=True, default=None)
    amount = models.IntegerField()
    price = models.FloatField()

class ShoppingCart(models.Model):
    items = models.ManyToManyField(Item)
    price = models.FloatField()

    def __str__(self):
        return self.id

class Order(models.Model):
    number = models.IntegerField()
    order = models.ForeignKey('ShoppingCart', on_delete=models.CASCADE, default=None)
    user = models.ForeignKey('User', on_delete=models.CASCADE, default=None)
    status = models.IntegerField(default=1)

    def __str__(self):
        return self.number
