# Competitions MODELS>PY

from django.db import models
from django.contrib.auth.models import User
import datetime


class Delivery(models.Model):
    name = models.Charfield(max_length=120)

    def __str(self):
        return self.name

    class Meta:
        verbose_name_plural = 'deliveries'



class Product(models.Model):
    owner = models.OneToManyField(User, on_delete=models.CASCADE)
    title = models.Charfield(max_length=100)
    description = models.TextField()
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    collection = models.Charfield(max_length=500, blank=True, null=True)
    min_ticket = models.IntegerField(default=1)
    max_ticket = models.IntegerField()
    quantity_winners = models.IntegerField(default=1)
    alternative_prize = models.Charfield(max_length=30, null=True, blank=True)
    end_date = models.DateField()
    tickets_bought = models.IntegerField()
    charity = models.Charfield(max_length=60)

    def __str__(self):
        return f'{self.user.username} Competition'


class Tickets(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    date = models.DateField(default=datetime.datetime.today)
    correct_answer = models.BooleanField(default=True)
    customer = models.ForeignKey(Users, on_delete=models.CASCADE)
    
