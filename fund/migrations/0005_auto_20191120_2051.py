# Generated by Django 2.2.7 on 2019-11-20 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fund', '0004_auto_20191120_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fundmaker',
            name='cs_number',
            field=models.CharField(max_length=13, null=True),
        ),
    ]