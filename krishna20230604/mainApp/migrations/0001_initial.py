# Generated by Django 4.2 on 2023-06-04 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Result",
            fields=[
                ("Rollno", models.IntegerField(primary_key=True, serialize=False)),
                ("Name", models.CharField(max_length=50)),
                ("Result", models.CharField(max_length=4)),
            ],
        ),
    ]