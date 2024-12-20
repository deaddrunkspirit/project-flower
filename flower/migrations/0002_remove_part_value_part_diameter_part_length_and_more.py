# Generated by Django 5.1.3 on 2024-11-13 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flower', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='part',
            name='value',
        ),
        migrations.AddField(
            model_name='part',
            name='diameter',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='part',
            name='length',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='part',
            name='thickness',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='part',
            name='material',
            field=models.CharField(default='Отсутствует', max_length=255),
        ),
        migrations.AlterField(
            model_name='part',
            name='name',
            field=models.CharField(default='Отсутствует', max_length=255),
        ),
        migrations.AlterField(
            model_name='part',
            name='weight',
            field=models.FloatField(default=1),
        ),
    ]
