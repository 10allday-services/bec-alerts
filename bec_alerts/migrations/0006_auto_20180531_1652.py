# Generated by Django 2.0.4 on 2018-05-31 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bec_alerts', '0005_auto_20180530_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='message',
            field=models.TextField(default=''),
        ),
    ]
