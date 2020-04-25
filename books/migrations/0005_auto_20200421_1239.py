# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_tender_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tender_info',
            name='url',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
