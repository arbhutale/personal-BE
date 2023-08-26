# Generated by Django 3.1.14 on 2023-08-26 20:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bank_account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankaccount',
            name='account_created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]