# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('element', models.IntegerField(choices=[(1, 'Fire'), (2, 'Water'), (3, 'Wind'), (4, 'Earth'), (5, 'Elec'), (6, 'Light'), (7, 'Dark'), (8, 'NoProp'), (9, 'Physical'), (10, 'Gun'), (11, 'Shadow')])),
                ('resist', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ItemAttribute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.IntegerField(default=0)),
                ('attr', models.ForeignKey(default=None, to='item.Attribute')),
                ('item', models.ForeignKey(to='item.Item')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
