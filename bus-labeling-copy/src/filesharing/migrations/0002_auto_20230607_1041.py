# Generated by Django 3.1 on 2023-06-07 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filesharing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='valid_until',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Valid Until'),
        ),
    ]