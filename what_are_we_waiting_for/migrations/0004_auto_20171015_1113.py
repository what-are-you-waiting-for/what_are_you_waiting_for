# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('what_are_we_waiting_for', '0003_auto_20171015_1012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dischargestep',
            name='received',
        ),
        migrations.RemoveField(
            model_name='dischargestep',
            name='received_timestamp',
        ),
        migrations.RemoveField(
            model_name='dischargestep',
            name='requested',
        ),
        migrations.RemoveField(
            model_name='dischargestep',
            name='requested_timestamp',
        ),
        migrations.RemoveField(
            model_name='dischargestep',
            name='specialist_type_fk',
        ),
        migrations.RemoveField(
            model_name='dischargestep',
            name='specialist_type_ft',
        ),
    ]
