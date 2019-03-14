# Generated by Django 2.1.7 on 2019-03-13 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("core", "0002_auto_20190313_1533")]

    operations = [
        migrations.AlterField(
            model_name="corerun",
            name="owner",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="sims",
                to="users.Profile",
            ),
        ),
        migrations.AlterField(
            model_name="corerun",
            name="project",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="sims",
                to="users.Project",
            ),
        ),
        migrations.AlterField(
            model_name="corerun",
            name="sponsor",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="sponsored_sims",
                to="users.Profile",
            ),
        ),
    ]