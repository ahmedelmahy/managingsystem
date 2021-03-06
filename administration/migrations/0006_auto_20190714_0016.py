# Generated by Django 2.2 on 2019-07-14 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0005_auto_20190709_0007'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='level',
            field=models.IntegerField(choices=[(1, 'clerk'), (2, 'leader'), (3, 'superVisor')], default=1),
        ),
        migrations.AddField(
            model_name='swaprequest',
            name='admin_answer',
            field=models.BooleanField(default=False),
        ),
    ]
