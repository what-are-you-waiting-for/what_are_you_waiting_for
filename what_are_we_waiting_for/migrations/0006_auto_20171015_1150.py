# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('what_are_we_waiting_for', '0005_auto_20171015_1120'),
    ]

    operations = [
        migrations.CreateModel(
            name='DischargeType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='dischargestep',
            name='discharge_type_fk',
            field=models.ForeignKey(blank=True, to='what_are_we_waiting_for.DischargeType', null=True),
        ),
    ]
