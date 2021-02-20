# Generated by Django 2.0.13 on 2019-07-23 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DOFs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dof_txt', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Stages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage_text', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_text', models.CharField(max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='stages',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ModelPlotter.Types'),
        ),
        migrations.AddField(
            model_name='dofs',
            name='stage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ModelPlotter.Stages'),
        ),
        migrations.AddField(
            model_name='dofs',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ModelPlotter.Types'),
        ),
    ]
