# Generated by Django 4.2.3 on 2023-07-28 09:23

from django.db import migrations, models
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Room",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "room_type",
                    model_utils.fields.StatusField(
                        choices=[
                            ("flat", "flat"),
                            ("1Room", "1Room"),
                            ("2Room", "2Room"),
                        ],
                        default="flat",
                        max_length=100,
                        no_check_for_status=True,
                    ),
                ),
                ("description", models.TextField(blank=True, null=True)),
                ("location", models.CharField(max_length=255)),
                ("price", models.DecimalField(decimal_places=2, max_digits=20)),
                (
                    "image",
                    models.ImageField(
                        blank=True, default="default_image.jpg", upload_to="uploads/"
                    ),
                ),
            ],
        ),
    ]