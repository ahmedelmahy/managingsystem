# Generated by Django 2.2 on 2019-07-29 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0017_log'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='afternoon',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='employee',
            name='evening',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='employee',
            name='morring',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='group',
            name='afternoon',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='group',
            name='evening',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='group',
            name='morring',
            field=models.IntegerField(default=0),
        ),
    ]