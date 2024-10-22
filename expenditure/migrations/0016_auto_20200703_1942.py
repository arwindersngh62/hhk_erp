# Generated by Django 2.2.3 on 2020-07-03 14:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('expenditure', '0015_auto_20200703_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advanced',
            name='added_on',
            field=models.DateField(default=datetime.datetime(2020, 7, 3, 14, 12, 29, 91067, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='approved',
            name='approval_date',
            field=models.DateField(verbose_name=datetime.datetime(2020, 7, 3, 14, 12, 29, 91067, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cleared',
            name='cleared_date',
            field=models.DateField(verbose_name=datetime.datetime(2020, 7, 3, 14, 12, 29, 101063, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='expenditure',
            name='added_on',
            field=models.DateField(default=datetime.datetime(2020, 7, 3, 14, 12, 29, 91067, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='expenditure',
            name='bill_date',
            field=models.DateField(default=datetime.datetime(2020, 7, 3, 14, 12, 29, 91067, tzinfo=utc)),
        ),
    ]
