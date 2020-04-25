# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20200420_1350'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meishi1',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('food_name', models.CharField(max_length=30)),
                ('food_author', models.CharField(max_length=8)),
                ('food_money', models.FloatField()),
                ('food_star', models.CharField(max_length=10, default='普通')),
            ],
        ),
    ]
