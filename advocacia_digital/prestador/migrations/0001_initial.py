# Generated by Django 4.2.5 on 2023-10-24 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anexo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('anexo', models.FileField(blank=True, null=True, upload_to='anexos/%Y/%m')),
            ],
        ),
        migrations.CreateModel(
            name='Atualizacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalhes', models.TextField()),
                ('explicacao', models.TextField(verbose_name='Explicação')),
                ('explicado', models.BooleanField(default=False)),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Atualização',
                'verbose_name_plural': 'Atualizações',
            },
        ),
        migrations.CreateModel(
            name='Docs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Documentos',
                'verbose_name_plural': 'Documentos',
            },
        ),
        migrations.CreateModel(
            name='Processo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=255)),
                ('tribunal', models.CharField(max_length=255)),
                ('ativo', models.BooleanField(default=False)),
            ],
        ),
    ]
