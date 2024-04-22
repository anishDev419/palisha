# Generated by Django 4.2.5 on 2024-04-02 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
        ("heroes", "0002_showcase"),
    ]

    operations = [
        migrations.CreateModel(
            name="ShowcasedProduct",
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
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                    ),
                ),
                (
                    "showcase",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="showcased_products",
                        to="heroes.showcase",
                    ),
                ),
            ],
        ),
    ]
