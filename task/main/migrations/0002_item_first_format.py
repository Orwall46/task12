# Generated by Django 4.1.4 on 2022-12-12 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='first_format',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Старый формат'),
        ),
    ]