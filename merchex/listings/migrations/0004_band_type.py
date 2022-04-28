# Generated by Django 4.0.4 on 2022-04-28 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_band_active_band_biography_band_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='type',
            field=models.CharField(choices=[('disques', 'Records'), ('vêtements', 'Clothings'), ('affiches', 'Posters'), ('divers', 'Micellaneous')], default='', max_length=20),
            preserve_default=False,
        ),
    ]
