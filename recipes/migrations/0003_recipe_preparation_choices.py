# Generated by Django 4.0.5 on 2022-06-16 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_recipe_servings_choices'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='preparation_choices',
            field=models.CharField(choices=[('Min', 'Minutos'), ('Hr', 'Horas')], default='', max_length=12),
        ),
    ]
