# Generated by Django 2.1.4 on 2018-12-26 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0004_auto_20181224_1415'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advert',
            options={},
        ),
        migrations.AddField(
            model_name='advert',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='user_pic'),
        ),
    ]
