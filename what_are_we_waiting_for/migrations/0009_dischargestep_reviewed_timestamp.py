# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('what_are_we_waiting_for', '0008_dischargestep_reviewed'),
    ]

    operations = [
        migrations.AddField(
            model_name='dischargestep',
            name='reviewed_timestamp',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
