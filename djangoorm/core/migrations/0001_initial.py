# Generated by Django 2.2.4 on 2020-01-14 02:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chassi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(help_text='Máximo 16 caracteres', max_length=16, verbose_name='Chassi')),
            ],
            options={
                'verbose_name': 'Chassi',
                'verbose_name_plural': 'Chassis',
            },
        ),
        migrations.CreateModel(
            name='Montadora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Montadora',
                'verbose_name_plural': 'Montadoras',
            },
        ),
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(help_text='Máximo 30 caracteres', max_length=30, verbose_name='Modelo')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço')),
                ('chassi', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Chassi')),
                ('montadora', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='core.Montadora')),
            ],
            options={
                'verbose_name': 'Carro',
                'verbose_name_plural': 'Carros',
            },
        ),
    ]
