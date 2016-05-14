# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pub_date',
            field=models.DateField(verbose_name='发表时间', auto_now_add=True, default=datetime.datetime(2016, 5, 12, 2, 0, 26, 385848, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='update_time',
            field=models.DateField(verbose_name='更新时间', null=True, auto_now=True),
        ),
    ]
