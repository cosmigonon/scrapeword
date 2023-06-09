# Generated by Django 4.1.7 on 2023-05-23 03:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "dashboard",
            "0004_transglossary_userglossary_remove_glossaryword_deck_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="userdeck",
            name="slug",
            field=models.SlugField(null=True),
        ),
        migrations.AddField(
            model_name="userglossary",
            name="slug",
            field=models.SlugField(null=True),
        ),
        migrations.AddField(
            model_name="userglossary",
            name="target_language",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name="userglossary",
            name="translation",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="userglossary",
            name="source_language",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.DeleteModel(
            name="TransGlossary",
        ),
    ]
