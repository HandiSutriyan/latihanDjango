# Generated by Django 3.0.2 on 2020-01-10 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20200110_0812'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='courses',
            new_name='choices',
        ),
    ]
