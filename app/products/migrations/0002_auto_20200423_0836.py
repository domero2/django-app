# Generated by Django 3.0.5 on 2020-04-23 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productone',
            old_name='cena',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='productone',
            old_name='nazwa',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='productone',
            old_name='opis',
            new_name='supplier',
        ),
        migrations.AddField(
            model_name='productone',
            name='description',
            field=models.TextField(default='CocaCola'),
        ),
    ]
