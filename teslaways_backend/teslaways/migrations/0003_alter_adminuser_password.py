# Generated by Django 4.0.1 on 2022-02-07 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teslaways', '0002_adminuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminuser',
            name='password',
            field=models.CharField(max_length=255),
        ),
    ]
