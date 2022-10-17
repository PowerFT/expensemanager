# Generated by Django 4.1.1 on 2022-10-14 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseCategory',
            fields=[
                ('mainid', models.AutoField(primary_key=True, serialize=False)),
                ('categoryname', models.CharField(max_length=30)),
                ('dateandtime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='IncomeCategory',
            fields=[
                ('mainid', models.AutoField(primary_key=True, serialize=False)),
                ('categoryname', models.CharField(max_length=30)),
                ('dateandtime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('mainid', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.FloatField()),
                ('description', models.TextField()),
                ('dateandtime', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expenseapp.incomecategory')),
            ],
        ),
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('mainid', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.FloatField()),
                ('description', models.TextField()),
                ('dateandtime', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expenseapp.expensecategory')),
            ],
        ),
    ]