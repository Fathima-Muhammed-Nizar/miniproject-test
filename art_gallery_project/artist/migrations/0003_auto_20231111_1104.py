# Generated by Django 3.0.7 on 2023-11-11 05:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0002_auto_20231110_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=150),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
