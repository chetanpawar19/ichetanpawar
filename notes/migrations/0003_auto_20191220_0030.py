# Generated by Django 2.2.7 on 2019-12-19 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20191219_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='notes',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]