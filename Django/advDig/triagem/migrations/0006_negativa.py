# Generated by Django 4.2.5 on 2023-10-27 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('triagem', '0005_pendencia_chave_pendencia_tipo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Negativa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('ref', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='triagem.demanda')),
            ],
        ),
    ]
