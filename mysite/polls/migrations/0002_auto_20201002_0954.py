# Generated by Django 3.1.2 on 2020-10-02 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choixe_text',
            new_name='choice_text',
        ),
    ]
