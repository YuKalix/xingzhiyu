# Generated by Django 2.1 on 2019-06-14 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('success_case', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='case',
            old_name='is_delete',
            new_name='is_display',
        ),
    ]
