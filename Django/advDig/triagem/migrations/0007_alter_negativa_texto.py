# Generated by Django 4.2.5 on 2023-10-30 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triagem', '0006_negativa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='negativa',
            name='texto',
            field=models.TextField(verbose_name='Justificativa para rejeição'),
        ),
    ]