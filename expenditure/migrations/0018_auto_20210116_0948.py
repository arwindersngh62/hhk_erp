# Generated by Django 3.1.3 on 2021-01-16 08:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('expenditure', '0017_auto_20210116_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advanced',
            name='added_on',
            field=models.DateField(default=datetime.datetime(2021, 1, 16, 8, 48, 2, 70405, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='approved',
            name='approval_date',
            field=models.DateField(verbose_name=datetime.datetime(2021, 1, 16, 8, 48, 2, 86033, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cleared',
            name='cleared_date',
            field=models.DateField(verbose_name=datetime.datetime(2021, 1, 16, 8, 48, 2, 86033, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='expenditure',
            name='added_on',
            field=models.DateField(default=datetime.datetime(2021, 1, 16, 8, 48, 2, 70405, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='expenditure',
            name='bill_date',
            field=models.DateField(default=datetime.datetime(2021, 1, 16, 8, 48, 2, 70405, tzinfo=utc)),
        ),
    ]