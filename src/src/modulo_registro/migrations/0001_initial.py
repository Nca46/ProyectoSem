# Generated by Django 4.2.5 on 2023-10-26 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.CharField(choices=[('lunes', 'Lunes'), ('martes', 'Martes'), ('miercoles', 'Miercoles'), ('jueves', 'Jueves'), ('viernes', 'Viernes'), ('sabado', 'Sabado'), ('domingo', 'Domingo')], max_length=10, verbose_name='Dias')),
                ('horario_inicio', models.TimeField(verbose_name='Horario Inicio')),
                ('horario_fin', models.TimeField(verbose_name='Horario Fin')),
            ],
        ),
        migrations.CreateModel(
            name='Retraso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=256, verbose_name='Titulo')),
                ('dia', models.DateTimeField(verbose_name='Dia')),
                ('descripcion', models.CharField(max_length=256, verbose_name='Descripcion')),
            ],
        ),
        migrations.CreateModel(
            name='Laboral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turno', models.CharField(max_length=256)),
                ('horarios', models.ManyToManyField(to='modulo_registro.horario')),
            ],
        ),
    ]