# Generated by Django 3.2 on 2022-11-16 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diplomatura', '0005_auto_20221110_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='estado',
            field=models.CharField(choices=[('Borr', 'Borrador'), ('Publi', 'Publicado'), ('Ret', 'Retirado')], default='Borrador', max_length=10),
        ),
    ]