# Generated by Django 3.2 on 2021-05-17 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_tablebooking_rest_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderfood',
            name='rest_name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]