# Generated by Django 4.0.1 on 2022-01-18 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crud_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="inventoryitem",
            name="archived",
            field=models.BooleanField(default=False),
        ),
    ]
