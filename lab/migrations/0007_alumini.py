# Generated by Django 3.2.7 on 2021-10-06 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0006_alter_joinus_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='alumini',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('labalumini', models.CharField(max_length=300, null=True)),
                ('currently', models.CharField(max_length=500, null=True)),
            ],
        ),
    ]
