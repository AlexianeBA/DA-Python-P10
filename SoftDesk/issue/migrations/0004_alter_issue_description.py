# Generated by Django 5.0.1 on 2024-01-21 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issue', '0003_alter_issue_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='description',
            field=models.TextField(max_length=1028),
        ),
    ]