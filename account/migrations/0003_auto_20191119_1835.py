# Generated by Django 2.2.7 on 2019-11-19 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_delete_maker'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialPlatform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(default=0, max_length=20)),
            ],
            options={
                'db_table': 'social_platform',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='social',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to='account.SocialPlatform'),
        ),
    ]