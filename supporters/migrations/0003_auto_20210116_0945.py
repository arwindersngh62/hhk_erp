# Generated by Django 3.1.3 on 2021-01-16 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supporters', '0002_auto_20200703_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supporter',
            name='amount',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='supporter',
            name='last_generated',
            field=models.IntegerField(default=0),
        ),
    ]
