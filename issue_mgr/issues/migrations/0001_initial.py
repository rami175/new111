# Generated by Django 5.0.6 on 2024-05-13 05:48

from django.db import migrations

def populate_status(apps, schemaeditor):
    entries = {
        "to do": "An issue for which work has not yet begun",
        "in progress": "An issue actively being worked on",
        "done": "An issue that has been completed" 
    }
    Status = apps.get_model("issues", "Status")
    for key, value in entries.items():
        status_obj = Status(name=key, description=value)
        status_obj.save()
class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [migrations.RunPython(populate_status)
    ]