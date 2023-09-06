# Competitions MODELS>PY

from django.db import models
from django.contrib.auth.models import User
import datetime


class Delivery(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'deliveries'



class Product(models.Model):
    owner = models.ManyToManyField(User)
    title = models.CharField(max_length=100)
    description = models.TextField()
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    collection = models.CharField(max_length=500, blank=True, null=True)
    min_ticket = models.IntegerField(default=1)
    max_ticket = models.IntegerField()
    quantity_winners = models.IntegerField(default=1)
    alternative_prize = models.CharField(max_length=30, null=True, blank=True)
    end_date = models.DateField()
    tickets_bought = models.IntegerField()
    charity = models.CharField(max_length=60)
    char_percent = models.IntegerField()

    def __str__(self):
        return str(self.title)


class TicketOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    date = models.DateField(default=datetime.datetime.today)
    correct_answer = models.BooleanField(default=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __int__(self):
        return str(self.id)
 

class CharPercent(models.Model):
    amount = models.IntegerField(default=0)

    def __str__(self):
        return str(self.amount)


