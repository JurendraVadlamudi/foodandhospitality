# Generated by Django 3.2 on 2021-05-11 17:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0007_auto_20210511_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uprofile',
            name='meta',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
