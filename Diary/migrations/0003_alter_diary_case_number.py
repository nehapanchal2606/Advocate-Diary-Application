# Generated by Django 4.1.1 on 2022-10-02 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Diary', '0002_diary_case_des'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='case_number',
            field=models.IntegerField(),
        ),
    ]
