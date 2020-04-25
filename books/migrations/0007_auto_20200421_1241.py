# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20200421_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tender_info',
            name='company',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tender_info',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tender_info',
            name='release_time',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tender_info',
            name='view_cont',
            field=models.CharField(max_length=100),
        ),
    ]
