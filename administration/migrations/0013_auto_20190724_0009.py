# Generated by Django 2.2 on 2019-07-24 00:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0012_remove_employee_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee_certification',
            name='certification',
        ),
        migrations.RemoveField(
            model_name='employee_certification',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='groupstatus',
            name='group',
        ),
        migrations.DeleteModel(
            name='Certification',
        ),
        migrations.DeleteModel(
            name='Employee_Certification',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.DeleteModel(
            name='GroupStatus',
        ),
    ]