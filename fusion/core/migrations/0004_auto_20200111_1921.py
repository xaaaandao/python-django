# Generated by Django 2.2.4 on 2020-01-11 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_feature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='icone',
            field=models.TextField(choices=[('lni-cog', 'Engrenagem'), ('lni-rocket', 'Foguete'), ('lni-laptop-phone', 'PC/Mobile'), ('lni-leaf', 'Folha'), ('lni-layers', 'Linhas')], max_length=16, verbose_name='Icone'),
        ),
    ]
