# Generated by Django 4.1.1 on 2023-02-27 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sch', '0037_week_hours_alter_shiftpreference_shift_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='data',
            field=models.JSONField(default={'emusr': 0, 'mistemplated': 0, 'n_empty': 0, 'percent': 0, 'pto_conflicts': 0, 'unfavorables': 0}),
        ),
    ]
