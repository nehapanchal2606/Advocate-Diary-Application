# Generated by Django 4.1.1 on 2022-10-01 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Diary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='case_des',
            field=models.TextField(default=-1),
            preserve_default=False,
        ),
    ]
