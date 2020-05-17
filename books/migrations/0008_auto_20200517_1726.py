# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20200421_1241'),
    ]

    operations = [
        migrations.CreateModel(
            name='spider_status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('spider_flag', models.IntegerField()),
                ('progress', models.IntegerField()),
                ('total_progress', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='tender_info',
            name='view_cont',
            field=models.IntegerField(max_length=100),
        ),
    ]
