# Generated by Django 2.2.3 on 2020-06-14 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('supporters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='verified_donation',
            fields=[
                ('rec_no', models.AutoField(primary_key=True, serialize=False)),
                ('anon_name', models.CharField(blank=True, max_length=100, null=True)),
                ('amount', models.CharField(max_length=20)),
                ('date_donation', models.DateField()),
                ('mode_donation', models.CharField(choices=[('CASH', 'Cash'), ('INET', 'Internet Banking'), ('UPI', 'UPI'), ('IMPS', 'IMPS'), ('NEFT', 'NEFT'), ('CHEQUE', 'Cheque')], default='CASH', max_length=100)),
                ('date_rec', models.DateField()),
                ('migrated', models.BooleanField(default=False)),
                ('anon', models.BooleanField(default=False)),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='supporters.supporter')),
            ],
        ),
    ]
