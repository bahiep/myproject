# Generated by Django 3.0.5 on 2021-09-01 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_withdraw'),
    ]

    operations = [
        migrations.AddField(
            model_name='withdraw',
            name='status',
            field=models.CharField(default='Đang xử lý', max_length=250),
        ),
    ]
