# Generated by Django 4.2.5 on 2023-12-05 20:22

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('room_api', '0009_bookedroom_room_is_booked_delete_booking_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='is_assigned',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='AssignedBookedRoom',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('assign_date', models.DateTimeField(auto_now_add=True)),
                ('booked_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booked_assignment', to='room_api.bookedroom')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_bookings', to='room_api.room')),
            ],
        ),
    ]
