# Generated by Django 2.2.18 on 2021-03-05 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("peeringdb_server", "0067_add_email_to_org_key"),
    ]

    operations = [
        migrations.AddField(
            model_name="facility",
            name="aka",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="Also Known As"
            ),
        ),
        migrations.AddField(
            model_name="facility",
            name="name_long",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="Long Name"
            ),
        ),
        migrations.AddField(
            model_name="internetexchange",
            name="aka",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="Also Known As"
            ),
        ),
        migrations.AddField(
            model_name="network",
            name="name_long",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="Long Name"
            ),
        ),
        migrations.AddField(
            model_name="organization",
            name="aka",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="Also Known As"
            ),
        ),
        migrations.AddField(
            model_name="organization",
            name="name_long",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="Long Name"
            ),
        ),
        migrations.AlterField(
            model_name="internetexchange",
            name="name_long",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="Long Name"
            ),
        ),
    ]