# Generated by Django 4.1.1 on 2022-09-19 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sch", "0005_ptorequest_datecreated_ptorequest_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ptorequest",
            name="workday",
            field=models.DateField(),
        ),
    ]
