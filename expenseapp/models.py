from unicodedata import category
from django.db import models

# Create your models here.
class ExpenseCategory(models.Model):
    mainid = models.AutoField(primary_key=True)
    categoryname = models.CharField(max_length=30)
    dateandtime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.categoryname

class Expenses(models.Model):
    mainid = models.AutoField(primary_key=True)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    amount = models.FloatField()
    description = models.TextField()
    dateandtime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category} {self.amount}"

class IncomeCategory(models.Model):
    mainid = models.AutoField(primary_key=True)
    categoryname = models.CharField(max_length=30)
    dateandtime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.categoryname

class Income(models.Model):
    mainid = models.AutoField(primary_key=True)
    category = models.ForeignKey(IncomeCategory, on_delete=models.CASCADE)
    amount = models.FloatField()
    description = models.TextField()
    dateandtime = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.category} {self.amount}"

