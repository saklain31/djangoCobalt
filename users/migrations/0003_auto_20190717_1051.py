# Generated by Django 2.0 on 2019-07-17 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_event'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'permissions': (('add_ev', 'Add event'), ('del_ev', 'Delete event'), ('edit_ev', 'Edit event'))},
        ),
    ]