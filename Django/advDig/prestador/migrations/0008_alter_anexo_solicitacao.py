# Generated by Django 4.2.5 on 2023-10-31 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prestador', '0007_alter_solicitacao_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anexo',
            name='solicitacao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prestador.solicitacao', verbose_name='Solicitação'),
        ),
    ]
