# Generated by Django 2.2.3 on 2020-06-15 06:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('expenditure', '0004_auto_20200615_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='advanced',
            name='amount_paid',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='advanced',
            name='added_on',
            field=models.DateField(default=datetime.datetime(2020, 6, 15, 6, 9, 25, 952768, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='approved',
            name='approval_date',
            field=models.DateField(verbose_name=datetime.datetime(2020, 6, 15, 6, 9, 25, 952768, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cleared',
            name='cleared_date',
            field=models.DateField(verbose_name=datetime.datetime(2020, 6, 15, 6, 9, 25, 952768, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='expenditure',
            name='added_on',
            field=models.DateField(default=datetime.datetime(2020, 6, 15, 6, 9, 25, 952768, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='expenditure',
            name='bill_date',
            field=models.DateField(default=datetime.datetime(2020, 6, 15, 6, 9, 25, 952768, tzinfo=utc)),
        ),
    ]
