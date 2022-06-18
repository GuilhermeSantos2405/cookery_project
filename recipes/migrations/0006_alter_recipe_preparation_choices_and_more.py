# Generated by Django 4.0.5 on 2022-06-18 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_alter_recipe_preparation_choices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='preparation_choices',
            field=models.CharField(choices=[('Minutos', 'Minutos'), ('Hora(s)', 'Hora(s)')], default='', max_length=12),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='servings_choices',
            field=models.CharField(choices=[('Unidade(s)', 'Unidade(s)'), ('Porções', 'Porções'), ('Pessoa(s)', 'Pessoa(s)')], default='', max_length=12),
        ),
    ]