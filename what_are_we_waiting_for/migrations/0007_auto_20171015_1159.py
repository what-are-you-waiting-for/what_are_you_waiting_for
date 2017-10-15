# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('what_are_we_waiting_for', '0006_auto_20171015_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='dischargestep',
            name='destination_type_fk',
            field=models.ForeignKey(blank=True, to='what_are_we_waiting_for.DestinationType', null=True),
        ),
        migrations.AddField(
            model_name='dischargestep',
            name='destination_type_ft',
            field=models.CharField(default=b'', max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='dischargestep',
            name='transport_type_fk',
            field=models.ForeignKey(blank=True, to='what_are_we_waiting_for.TransportType', null=True),
        ),
        migrations.AddField(
            model_name='dischargestep',
            name='transport_type_ft',
            field=models.CharField(default=b'', max_length=255, null=True, blank=True),
        ),
    ]
