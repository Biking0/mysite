# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20200421_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tender_info',
            name='url',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
