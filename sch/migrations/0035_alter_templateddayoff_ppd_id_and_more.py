# Generated by Django 4.1.1 on 2022-10-21 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sch', '0034_templateddayoff_sd_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='templateddayoff',
            name='ppd_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='templateddayoff',
            name='sd_id',
            field=models.IntegerField(),
        ),
        migrations.AlterUniqueTogether(
            name='templateddayoff',
            unique_together={('employee', 'sd_id')},
        ),
    ]
