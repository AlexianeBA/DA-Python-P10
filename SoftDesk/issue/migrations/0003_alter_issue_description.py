# Generated by Django 5.0.1 on 2024-01-21 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issue', '0002_alter_issue_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='description',
            field=models.TextField(),
        ),
    ]
