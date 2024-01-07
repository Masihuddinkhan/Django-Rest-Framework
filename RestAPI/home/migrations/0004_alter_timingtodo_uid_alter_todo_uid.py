# Generated by Django 4.2.7 on 2023-12-31 15:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_todo_uid_timingtodo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timingtodo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('4f49d6e9-fb31-4636-ac00-af6613aa5786'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('4f49d6e9-fb31-4636-ac00-af6613aa5786'), editable=False, primary_key=True, serialize=False),
        ),
    ]