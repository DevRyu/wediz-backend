# Generated by Django 2.2.7 on 2019-11-22 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileInterest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education_kids', models.BooleanField()),
                ('fashion_beauty_goods', models.BooleanField()),
                ('home_design_item', models.BooleanField()),
                ('concert_culture', models.BooleanField()),
                ('sport_mobility', models.BooleanField()),
                ('publishing', models.BooleanField()),
                ('animal', models.BooleanField()),
                ('tech_home_appliance', models.BooleanField()),
            ],
            options={
                'db_table': 'profileinterests',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255, unique=True)),
                ('user_name', models.CharField(blank=True, max_length=150, null=True)),
                ('password', models.CharField(blank=True, max_length=300, null=True)),
                ('phone_number', models.CharField(max_length=20, null=True)),
                ('is_agree', models.BooleanField(null=True)),
                ('is_maker', models.BooleanField(null=True)),
                ('promotion', models.BooleanField(null=True)),
                ('profile_photo', models.URLField(blank=True, max_length=500, null=True)),
                ('company', models.CharField(blank=True, max_length=100, null=True)),
                ('company_position', models.CharField(blank=True, max_length=50, null=True)),
                ('university', models.CharField(blank=True, max_length=50, null=True)),
                ('major', models.CharField(blank=True, max_length=50, null=True)),
                ('main_address', models.CharField(blank=True, max_length=50, null=True)),
                ('sub_address', models.CharField(blank=True, max_length=50, null=True)),
                ('introduction', models.CharField(blank=True, max_length=1200, null=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='UserGetInterest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_interest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.ProfileInterest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.User')),
            ],
            options={
                'db_table': 'usergetinterests',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='user_interest',
            field=models.ManyToManyField(through='account.UserGetInterest', to='account.ProfileInterest'),
        ),
        migrations.CreateModel(
            name='Maker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('kind', models.CharField(max_length=150)),
                ('phone_number', models.IntegerField()),
                ('is_agreed', models.BooleanField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='account.User')),
            ],
            options={
                'db_table': 'makers',
            },
        ),
    ]
