# Generated by Django 4.1.2 on 2022-10-19 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("url_trimmer", "0004_saveurl_created_at_alter_saveurl_alias"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="saveurl",
            options={"ordering": ("created_at",)},
        ),
    ]
