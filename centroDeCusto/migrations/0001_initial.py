# Generated by Django 2.2.18 on 2021-02-10 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CentroDeCusto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('centroDeCusto', models.CharField(max_length=100, verbose_name='Centro de custo')),
            ],
        ),
    ]
