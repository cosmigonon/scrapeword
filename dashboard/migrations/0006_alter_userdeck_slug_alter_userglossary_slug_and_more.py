# Generated by Django 4.1.7 on 2023-05-23 03:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0005_userdeck_slug_userglossary_slug_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userdeck",
            name="slug",
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name="userglossary",
            name="slug",
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name="userglossary",
            name="source_language",
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name="userglossary",
            name="target_language",
            field=models.CharField(max_length=2),
        ),
    ]
