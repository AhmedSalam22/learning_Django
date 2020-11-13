# Generated by Django 3.0 on 2020-09-01 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0004_auto_20160126_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='level',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='account',
            name='lft',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='account',
            name='rght',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='account',
            name='type',
            field=models.CharField(choices=[('As', 'Asset'), ('Eq', 'Equity'), ('NE', 'Net earnings'), ('Li', 'Liability'), ('In', 'Income'), ('Ex', 'Expense')], max_length=2),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='state',
            field=models.CharField(choices=[('D', 'Draft'), ('C', 'Committed')], default='D', editable=False, max_length=1),
        ),
        migrations.AlterField(
            model_name='transactionitem',
            name='account',
            field=models.ForeignKey(limit_choices_to={'frozen': False}, on_delete=django.db.models.deletion.PROTECT, to='accounting.Account'),
        ),
    ]