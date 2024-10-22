# Generated by Django 3.1.3 on 2021-03-28 05:26

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('usersreg', '0001_initial'),
        ('exptemp', '0004_auto_20210327_2012'),
    ]

    operations = [
        migrations.CreateModel(
            name='settled',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('settle_date', models.DateField(verbose_name=datetime.datetime(2021, 3, 28, 5, 26, 6, 239477, tzinfo=utc))),
                ('payment_date', models.DateField()),
                ('expense_head', models.CharField(max_length=250)),
                ('category', models.CharField(max_length=250)),
                ('sub_category', models.CharField(max_length=250)),
                ('amount_approved', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('settled_comments', models.CharField(max_length=1000)),
                ('settled_by', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='usersreg.member')),
            ],
        ),
        migrations.AlterField(
            model_name='expense',
            name='added_on',
            field=models.DateField(default=datetime.datetime(2021, 3, 28, 5, 26, 6, 239477, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='approved',
        ),
        migrations.AddField(
            model_name='expense',
            name='exp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exptemp.settled'),
        ),
    ]
