# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('what_are_we_waiting_for', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imaging',
            old_name='received',
            new_name='reviewed',
        ),
        migrations.RenameField(
            model_name='imaging',
            old_name='received_timestamp',
            new_name='reviewed_timestamp',
        ),
        migrations.RenameField(
            model_name='labtest',
            old_name='received',
            new_name='reviewed',
        ),
        migrations.RenameField(
            model_name='labtest',
            old_name='received_timestamp',
            new_name='reviewed_timestamp',
        ),
        migrations.RenameField(
            model_name='specialistreview',
            old_name='received',
            new_name='reviewed',
        ),
        migrations.RenameField(
            model_name='specialistreview',
            old_name='received_timestamp',
            new_name='reviewed_timestamp',
        ),
    ]
