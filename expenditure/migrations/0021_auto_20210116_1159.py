# Generated by Django 3.1.3 on 2021-01-16 10:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('expenditure', '0020_auto_20210116_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advanced',
            name='added_on',
            field=models.DateField(default=datetime.datetime(2021, 1, 16, 10, 59, 16, 173679, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='approved',
            name='approval_date',
            field=models.DateField(verbose_name=datetime.datetime(2021, 1, 16, 10, 59, 16, 174679, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cleared',
            name='cleared_date',
            field=models.DateField(verbose_name=datetime.datetime(2021, 1, 16, 10, 59, 16, 175680, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='expenditure',
            name='added_on',
            field=models.DateField(default=datetime.datetime(2021, 1, 16, 10, 59, 16, 173679, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='expenditure',
            name='bill_date',
            field=models.DateField(default=datetime.datetime(2021, 1, 16, 10, 59, 16, 173679, tzinfo=utc)),
        ),
    ]