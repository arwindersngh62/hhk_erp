# Generated by Django 3.1.3 on 2021-03-27 19:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('exptemp', '0003_auto_20210327_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approved',
            name='settle_date',
            field=models.DateField(verbose_name=datetime.datetime(2021, 3, 27, 19, 12, 16, 295477, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='expense',
            name='added_on',
            field=models.DateField(default=datetime.datetime(2021, 3, 27, 19, 12, 16, 294478, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='expense',
            name='expense_date',
            field=models.DateField(null=True),
        ),
    ]