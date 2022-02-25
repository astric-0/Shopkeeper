# Generated by Django 3.2.8 on 2021-11-16 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('Color', models.CharField(max_length=10, null=True)),
                ('Series', models.CharField(default='P', max_length=5)),
                ('BoxId', models.IntegerField(primary_key=True, serialize=False)),
                ('ThreadCount', models.IntegerField(max_length=20, null=True)),
                ('BoxNumber', models.IntegerField(max_length=10, null=True)),
                ('Batch', models.IntegerField(max_length=10, null=True)),
            ],
        ),
    ]
