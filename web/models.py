from django.contrib.auth.models import User
from django.db import models


class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)
    amount = models.BigIntegerField()

    def __str__(self):
        return "{}-{}".format(self.token, self.amount)


class Expense(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCAD)

    def __str__(self):
        return "{}-{}-{}".format(self.text, self.amount, self.date)


class Income(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCAD)

    def __str__(self):
        return "{}-{}-{}".format(self.text, self.amount, self.date)
