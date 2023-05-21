# Generated by Django 4.2.1 on 2023-05-21 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('person', models.IntegerField(default=0)),
                ('menu1', models.IntegerField(default=0)),
                ('menu2', models.IntegerField(default=0)),
                ('menu3', models.IntegerField(default=0)),
                ('menu4', models.IntegerField(default=0)),
                ('drink1', models.IntegerField(default=0)),
                ('drink2', models.IntegerField(default=0)),
                ('drink3', models.IntegerField(default=0)),
                ('drink4', models.IntegerField(default=0)),
                ('total', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.IntegerField()),
                ('person', models.IntegerField(default=0)),
                ('menu1', models.IntegerField(default=0)),
                ('menu2', models.IntegerField(default=0)),
                ('menu3', models.IntegerField(default=0)),
                ('menu4', models.IntegerField(default=0)),
                ('drink1', models.IntegerField(default=0)),
                ('drink2', models.IntegerField(default=0)),
                ('drink3', models.IntegerField(default=0)),
                ('drink4', models.IntegerField(default=0)),
                ('total', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Total',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('person', models.IntegerField(default=0)),
                ('menu1', models.IntegerField(default=0)),
                ('menu2', models.IntegerField(default=0)),
                ('menu3', models.IntegerField(default=0)),
                ('menu4', models.IntegerField(default=0)),
                ('drink1', models.IntegerField(default=0)),
                ('drink2', models.IntegerField(default=0)),
                ('drink3', models.IntegerField(default=0)),
                ('drink4', models.IntegerField(default=0)),
                ('total', models.IntegerField(default=0)),
            ],
        ),
    ]
