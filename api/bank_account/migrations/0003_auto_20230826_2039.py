# Generated by Django 3.1.14 on 2023-08-26 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_account', '0002_bankaccount_account_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankaccount',
            name='account_holder_name',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bankaccount',
            name='bank_name',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bankaccount',
            name='branch',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bankaccount',
            name='cheque_image',
            field=models.URLField(default=0, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bankaccount',
            name='ifsc_code',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bankaccount',
            name='passbook_image',
            field=models.URLField(default=0, max_length=250),
            preserve_default=False,
        ),
    ]