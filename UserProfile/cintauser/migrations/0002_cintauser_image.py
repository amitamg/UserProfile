# Generated by Django 3.1.7 on 2021-03-13 18:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cintauser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cintauser',
            name='image',
            field=models.FileField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]
