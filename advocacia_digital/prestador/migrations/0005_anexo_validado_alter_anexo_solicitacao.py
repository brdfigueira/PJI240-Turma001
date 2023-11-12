# Generated by Django 4.2.5 on 2023-10-30 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prestador', '0004_alter_anexo_demanda_alter_anexo_processo_solicitacao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='anexo',
            name='validado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='anexo',
            name='solicitacao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='prestador.solicitacao', verbose_name='Solicitação'),
        ),
    ]