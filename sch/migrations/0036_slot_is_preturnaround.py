# Generated by Django 4.1.1 on 2022-10-21 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sch', '0035_alter_templateddayoff_ppd_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='is_preturnaround',
            field=models.IntegerField(default=False, editable=False),
            preserve_default=False,
        ),
    ]
