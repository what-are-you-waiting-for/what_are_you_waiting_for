# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import opal.models


class Migration(migrations.Migration):

    dependencies = [
        ('opal', '0031_auto_20170719_1018'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('what_are_we_waiting_for', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractTestModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('requested', models.DateTimeField()),
                ('received', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='DischargeStep',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('created_by', models.ForeignKey(related_name='created_what_are_we_waiting_for_dischargestep_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('episode', models.ForeignKey(to='opal.Episode')),
                ('updated_by', models.ForeignKey(related_name='updated_what_are_we_waiting_for_dischargestep_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ImagingTestType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LabTestType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SpecialistType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='investigation',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='investigation',
            name='episode',
        ),
        migrations.RemoveField(
            model_name='investigation',
            name='updated_by',
        ),
        migrations.CreateModel(
            name='Imaging',
            fields=[
                ('abstracttestmodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='what_are_we_waiting_for.AbstractTestModel')),
                ('test_type_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('test_type_fk', models.ForeignKey(blank=True, to='what_are_we_waiting_for.ImagingTestType', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('what_are_we_waiting_for.abstracttestmodel',),
        ),
        migrations.CreateModel(
            name='LabTest',
            fields=[
                ('abstracttestmodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='what_are_we_waiting_for.AbstractTestModel')),
                ('test_type_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('test_type_fk', models.ForeignKey(blank=True, to='what_are_we_waiting_for.LabTestType', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('what_are_we_waiting_for.abstracttestmodel',),
        ),
        migrations.CreateModel(
            name='SpecialistReview',
            fields=[
                ('abstracttestmodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='what_are_we_waiting_for.AbstractTestModel')),
                ('specialist_type_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('specialist_type_fk', models.ForeignKey(blank=True, to='what_are_we_waiting_for.SpecialistType', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('what_are_we_waiting_for.abstracttestmodel',),
        ),
        migrations.DeleteModel(
            name='Investigation',
        ),
        migrations.AddField(
            model_name='abstracttestmodel',
            name='created_by',
            field=models.ForeignKey(related_name='created_what_are_we_waiting_for_abstracttestmodel_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='abstracttestmodel',
            name='episode',
            field=models.ForeignKey(to='opal.Episode'),
        ),
        migrations.AddField(
            model_name='abstracttestmodel',
            name='updated_by',
            field=models.ForeignKey(related_name='updated_what_are_we_waiting_for_abstracttestmodel_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
