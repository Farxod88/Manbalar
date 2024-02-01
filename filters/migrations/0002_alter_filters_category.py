# Generated by Django 5.0.1 on 2024-01-26 11:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_alter_categories_map'),
        ('filters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filters',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='categories.categories'),
        ),
    ]