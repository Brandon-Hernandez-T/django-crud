# Generated by Django 4.2.7 on 2024-01-11 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tescha', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiante',
            name='user',
        ),
        migrations.AlterField(
            model_name='curso',
            name='creditos',
            field=models.PositiveIntegerField(),
        ),
    ]
