from django.contrib import admin
from expenseapp.models import Expenses, Income, ExpenseCategory, IncomeCategory

# Register your models here.
admin.site.register(Expenses)
admin.site.register(Income)
admin.site.register(ExpenseCategory)
admin.site.register(IncomeCategory)
