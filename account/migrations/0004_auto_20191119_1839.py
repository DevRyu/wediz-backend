# Generated by Django 2.2.7 on 2019-11-19 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20191119_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialplatform',
            name='platform',
            field=models.CharField(default=1, max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='social',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='account.SocialPlatform'),
        ),
    ]
