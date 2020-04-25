# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_meishi1'),
    ]

    operations = [
        migrations.CreateModel(
            name='tender_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=30)),
                ('company', models.CharField(max_length=30)),
                ('view_cont', models.CharField(max_length=30)),
                ('release_time', models.CharField(max_length=30)),
                ('url', models.CharField(max_length=30)),
            ],
        ),
    ]
