# Generated by Django 4.2.5 on 2023-10-24 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('prestador', '0001_initial'),
        ('triagem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='processo',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='triagem.cliente', verbose_name='Cliente'),
        ),
        migrations.AddField(
            model_name='processo',
            name='demanda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='triagem.demanda', verbose_name='Queixa Original'),
        ),
        migrations.AddField(
            model_name='docs',
            name='anexos',
            field=models.ManyToManyField(to='prestador.anexo'),
        ),
        migrations.AddField(
            model_name='docs',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='triagem.cliente'),
        ),
        migrations.AddField(
            model_name='docs',
            name='demanda',
            field=models.ManyToManyField(to='triagem.demanda'),
        ),
        migrations.AddField(
            model_name='docs',
            name='processo',
            field=models.ManyToManyField(to='prestador.processo'),
        ),
        migrations.AddField(
            model_name='atualizacao',
            name='processo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='prestador.processo'),
        ),
        migrations.AddField(
            model_name='anexo',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='triagem.cliente'),
        ),
        migrations.AddField(
            model_name='anexo',
            name='demanda',
            field=models.ManyToManyField(to='triagem.demanda'),
        ),
        migrations.AddField(
            model_name='anexo',
            name='processo',
            field=models.ManyToManyField(to='prestador.processo'),
        ),
    ]