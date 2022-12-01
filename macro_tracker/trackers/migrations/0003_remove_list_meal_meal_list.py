# Generated by Django 4.1 on 2022-12-01 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trackers', '0002_remove_list_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='meal',
        ),
        migrations.AddField(
            model_name='meal',
            name='list',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meals_tracked', to='trackers.list'),
        ),
    ]