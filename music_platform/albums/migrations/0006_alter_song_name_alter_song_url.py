# Generated by Django 4.1.3 on 2022-11-14 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0005_song'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='song',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]