# Generated by Django 3.2.12 on 2022-03-06 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='document_sha1',
            field=models.CharField(default=123, max_length=40),
            preserve_default=False,
        ),
    ]
