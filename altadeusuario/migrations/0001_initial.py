# Generated by Django 3.1.7 on 2021-03-05 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AltaUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificacion', models.IntegerField()),
                ('Nombre', models.CharField(max_length=50)),
                ('Apellidos', models.CharField(max_length=50)),
                ('Puesto', models.CharField(max_length=50)),
                ('Horario', models.CharField(max_length=50)),
                ('Descanso', models.CharField(max_length=50)),
                ('Perfiles', models.CharField(choices=[('usuariotecnico', 'Usuario Técnico'), ('usuarioadministrador', 'Usuario Administrador')], default='usuarioadministrador', max_length=30)),
            ],
        ),
    ]
