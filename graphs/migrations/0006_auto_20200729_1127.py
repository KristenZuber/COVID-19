# Generated by Django 3.0.7 on 2020-07-29 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphs', '0005_auto_20200729_0226'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlPredict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m', models.FloatField(default=72.3261)),
                ('x', models.FloatField(default=1)),
                ('b', models.FloatField(default=4359.2334)),
            ],
        ),
        migrations.DeleteModel(
            name='Temps',
        ),
    ]
