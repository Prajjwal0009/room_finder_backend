# Generated by Django 4.2.3 on 2023-08-01 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("room_api", "0005_remove_contactus_nane_contactus_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contactus",
            name="phone",
            field=models.IntegerField(),
        ),
    ]
