# Generated by Django 2.2.12 on 2020-05-16 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='customerbookmark',
            unique_together={('customer', 'bookmark')},
        ),
    ]