# Generated by Django 2.2.3 on 2020-06-30 14:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('expenditure', '0012_auto_20200618_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advanced',
            name='added_on',
            field=models.DateField(default=datetime.datetime(2020, 6, 30, 14, 16, 19, 509777, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='approved',
            name='approval_date',
            field=models.DateField(verbose_name=datetime.datetime(2020, 6, 30, 14, 16, 19, 512776, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cleared',
            name='cleared_date',
            field=models.DateField(verbose_name=datetime.datetime(2020, 6, 30, 14, 16, 19, 512776, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='expenditure',
            name='added_on',
            field=models.DateField(default=datetime.datetime(2020, 6, 30, 14, 16, 19, 510777, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='expenditure',
            name='bill_date',
            field=models.DateField(default=datetime.datetime(2020, 6, 30, 14, 16, 19, 510777, tzinfo=utc)),
        ),
    ]