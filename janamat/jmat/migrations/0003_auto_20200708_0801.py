# Generated by Django 2.2.10 on 2020-07-08 02:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jmat', '0002_auto_20200708_0135'),
    ]

    operations = [
        migrations.DeleteModel(
            name='testMOdel',
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='vote',
            name='Chellenge',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='Topic',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='User',
        ),
        migrations.DeleteModel(
            name='TopicList',
        ),
        migrations.DeleteModel(
            name='Vote',
        ),
    ]