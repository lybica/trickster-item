# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_attribute_itemattribute'),
    ]

    operations = [
        migrations.CreateModel(
            name='DropItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rate', models.SmallIntegerField()),
                ('count', models.IntegerField()),
                ('drop', models.ForeignKey(to='item.Item')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PresentItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ptype', models.IntegerField()),
                ('count', models.IntegerField()),
                ('item', models.OneToOneField(to='item.Item')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='dropitem',
            name='item',
            field=models.ForeignKey(to='item.PresentItem'),
            preserve_default=True,
        ),
    ]
