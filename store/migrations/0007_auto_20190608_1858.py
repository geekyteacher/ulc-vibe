# Generated by Django 2.2.1 on 2019-06-08 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20190608_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productpicture',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
