# Generated by Django 2.0.13 on 2019-07-23 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ModelPlotter', '0002_auto_20190723_0246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dofs',
            name='type',
        ),
        migrations.AlterField(
            model_name='dofs',
            name='stage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ModelPlotter.Stages'),
        ),
    ]
