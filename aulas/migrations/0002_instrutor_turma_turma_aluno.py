# Generated by Django 3.2.5 on 2021-07-15 02:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aulas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instrutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60, unique=True)),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='aulas.curso')),
                ('instrutor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='aulas.instrutor')),
            ],
            options={
                'ordering': ['curso'],
            },
        ),
        migrations.CreateModel(
            name='Turma_Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='aulas.candidato')),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='aulas.turma')),
            ],
            options={
                'ordering': ['turma', 'aluno'],
            },
        ),
    ]
