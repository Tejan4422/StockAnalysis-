# Generated by Django 3.0.2 on 2020-01-20 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visualize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bidytext', models.TextField()),
                ('vcompanyname', models.CharField(max_length=100)),
                ('sdate', models.CharField(max_length=100)),
                ('edate', models.CharField(max_length=100)),
            ],
        ),
    ]