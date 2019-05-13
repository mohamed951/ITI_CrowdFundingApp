# Generated by Django 2.2.1 on 2019-05-13 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_reportedcomment_reportedproject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportedcomment',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='reportedcomment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='reportedproject',
            name='project',
        ),
        migrations.RemoveField(
            model_name='reportedproject',
            name='user',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='ReportedComment',
        ),
        migrations.DeleteModel(
            name='ReportedProject',
        ),
    ]
