# Generated by Django 3.2.7 on 2021-10-06 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0002_alter_researchpaper_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='researchpaper',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]
