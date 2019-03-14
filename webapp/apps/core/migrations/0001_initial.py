# Generated by Django 2.1.7 on 2019-03-13 20:28

import datetime
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [("users", "0005_auto_20190313_1528")]

    operations = [
        migrations.CreateModel(
            name="CoreInputs",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "meta_parameters",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        blank=True, default=None, null=True
                    ),
                ),
                (
                    "raw_gui_inputs",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        blank=True, default=None, null=True
                    ),
                ),
                (
                    "gui_inputs",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        blank=True, default=None, null=True
                    ),
                ),
                (
                    "inputs_file",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        blank=True, default=dict, null=True
                    ),
                ),
                (
                    "errors_warnings_text",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        blank=True, default=None, null=True
                    ),
                ),
                (
                    "upstream_parameters",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        blank=True, default=dict, null=True
                    ),
                ),
                (
                    "input_type",
                    models.CharField(
                        choices=[("paramtools", "paramtools"), ("taxcalc", "taxcalc")],
                        max_length=32,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CoreRun",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "meta_data",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        blank=True, default=None, null=True
                    ),
                ),
                (
                    "outputs",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        blank=True, default=None, null=True
                    ),
                ),
                (
                    "aggr_outputs",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        blank=True, default=None, null=True
                    ),
                ),
                (
                    "error_text",
                    models.CharField(
                        blank=True, default=None, max_length=4000, null=True
                    ),
                ),
                ("run_time", models.IntegerField(default=0)),
                (
                    "run_cost",
                    models.DecimalField(decimal_places=4, default=0.0, max_digits=9),
                ),
                (
                    "creation_date",
                    models.DateTimeField(
                        default=datetime.datetime(2015, 1, 1, 5, 0, tzinfo=utc)
                    ),
                ),
                (
                    "exp_comp_datetime",
                    models.DateTimeField(
                        default=datetime.datetime(2015, 1, 1, 5, 0, tzinfo=utc)
                    ),
                ),
                ("job_id", models.UUIDField(blank=True, default=None, null=True)),
                (
                    "upstream_vers",
                    models.CharField(
                        blank=True, default=None, max_length=50, null=True
                    ),
                ),
                (
                    "webapp_vers",
                    models.CharField(
                        blank=True, default=None, max_length=50, null=True
                    ),
                ),
                (
                    "inputs",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="outputs",
                        to="core.CoreInputs",
                    ),
                ),
                (
                    "profile",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="core_corerun_runs",
                        to="users.Profile",
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="core_corerun_runs",
                        to="users.Project",
                    ),
                ),
                (
                    "sponsor",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="core_corerun_sponsored_runs",
                        to="users.Profile",
                    ),
                ),
            ],
        ),
    ]