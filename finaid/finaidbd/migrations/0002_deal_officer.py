# Generated by Django 5.1 on 2024-09-03 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("finaidbd", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Deal_officer",
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
                ("name", models.CharField(max_length=64)),
                ("mobile", models.IntegerField()),
                ("pic", models.ImageField(blank=True, null=True, upload_to="images/")),
            ],
        ),
    ]
