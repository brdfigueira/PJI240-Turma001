# Generated by Django 4.2.5 on 2023-10-31 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('triagem', '0007_alter_negativa_texto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='demanda',
            old_name='info1',
            new_name='detalhes',
        ),
        migrations.RemoveField(
            model_name='demanda',
            name='info2',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='detalhes',
        ),
    ]