# Generated by Django 4.0.5 on 2022-06-16 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_alter_recipe_servings_choices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='preparation_choices',
            field=models.CharField(choices=[('Min', 'Minutos'), ('Hr', 'Hora(s)')], default='', max_length=12),
        ),
    ]
