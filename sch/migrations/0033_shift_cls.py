# Generated by Django 4.1.1 on 2022-10-21 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sch', '0032_employee_cls'),
    ]

    operations = [
        migrations.AddField(
            model_name='shift',
            name='cls',
            field=models.CharField(choices=[('CPhT', 'CPhT'), ('RPh', 'RPh')], max_length=5, null=True),
        ),
    ]
