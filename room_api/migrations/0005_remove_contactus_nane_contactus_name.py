# Generated by Django 4.2.3 on 2023-08-01 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("room_api", "0004_contactus"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="contactus",
            name="nane",
        ),
        migrations.AddField(
            model_name="contactus",
            name="name",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
