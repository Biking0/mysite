# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meishi',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('food_name', models.CharField(max_length=30)),
                ('food_author', models.CharField(max_length=8)),
                ('food_money', models.FloatField()),
                ('food_star', models.CharField(max_length=10, default='普通')),
            ],
        ),
        migrations.AlterModelOptions(
            name='publisher',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(max_length=254, blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='publication_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
