# Generated by Django 2.0.6 on 2018-07-29 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20180729_1615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='userid',
        ),
        migrations.DeleteModel(
            name='Login',
        ),
    ]