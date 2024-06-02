from django.db import migrations

# Generated by Django 5.0.6 on 2024-05-22 16:40



class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_blogpost_read_count'),
    ]

    operations = [
        migrations.RunSQL("UPDATE app_blogpost SET read_count = 1 WHERE read_count = 0;")
    ]