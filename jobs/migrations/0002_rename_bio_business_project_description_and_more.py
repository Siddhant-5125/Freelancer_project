# Generated by Django 5.1 on 2024-09-02 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='bio',
            new_name='project_description',
        ),
        migrations.AddField(
            model_name='business',
            name='domain',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='business',
            name='skills_required',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='freelancer',
            name='skills',
            field=models.TextField(blank=True),
        ),
    ]
