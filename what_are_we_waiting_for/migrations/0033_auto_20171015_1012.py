# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('what_are_we_waiting_for', '0032_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransportType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='dischargestep',
            name='received',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='dischargestep',
            name='received_timestamp',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='dischargestep',
            name='requested',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='dischargestep',
            name='requested_timestamp',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='dischargestep',
            name='specialist_type_ft',
            field=models.CharField(default=b'', max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='dischargestep',
            name='specialist_type_fk',
            field=models.ForeignKey(blank=True, to='what_are_we_waiting_for.TransportType', null=True),
        ),
    ]
