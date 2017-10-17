# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('what_are_we_waiting_for', '0007_auto_20171015_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='dischargestep',
            name='reviewed',
            field=models.NullBooleanField(),
        ),
    ]
