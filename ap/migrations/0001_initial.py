# Generated by Django 3.1 on 2022-02-04 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='female',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('favourite_color', models.CharField(max_length=100)),
                ('favourite_beauty_brand', models.CharField(max_length=100)),
                ('favourite_beauty_product', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='male',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('favourite_game', models.CharField(max_length=100)),
                ('favourite_sports_person', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('l_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
            ],
        ),
    ]
