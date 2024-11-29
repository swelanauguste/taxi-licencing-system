# Generated by Django 5.1.2 on 2024-10-25 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owners', '0003_remove_owner_state'),
        ('vehicles', '0003_vehicle_slug_alter_vehiclemake_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='owner',
            field=models.ManyToManyField(related_name='vehicles', to='owners.owner'),
        ),
    ]
