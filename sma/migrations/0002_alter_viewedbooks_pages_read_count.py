# Generated by Django 4.0.4 on 2022-06-17 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sma', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viewedbooks',
            name='pages_read_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
