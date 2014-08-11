# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemAttribute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fire', models.IntegerField()),
                ('water', models.IntegerField()),
                ('wind', models.IntegerField()),
                ('earth', models.IntegerField()),
                ('elec', models.IntegerField()),
                ('light', models.IntegerField()),
                ('dark', models.IntegerField()),
                ('noprop', models.IntegerField()),
                ('firer', models.IntegerField()),
                ('waterr', models.IntegerField()),
                ('windr', models.IntegerField()),
                ('earthr', models.IntegerField()),
                ('elecr', models.IntegerField()),
                ('lightr', models.IntegerField()),
                ('darkr', models.IntegerField()),
                ('nopropr', models.IntegerField()),
                ('physicalr', models.IntegerField()),
                ('gunr', models.IntegerField()),
                ('shadow', models.IntegerField()),
                ('shadowr', models.IntegerField()),
                ('item', models.ForeignKey(to='item.Item')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
