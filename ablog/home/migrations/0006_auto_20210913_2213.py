# Generated by Django 3.0.5 on 2021-09-13 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_withdraw_cashwithdraw'),
    ]

    operations = [
        migrations.AlterField(
            model_name='withdraw',
            name='cashwithdraw',
            field=models.IntegerField(default=0),
        ),
    ]
