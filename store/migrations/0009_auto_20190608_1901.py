# Generated by Django 2.2.1 on 2019-06-08 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_productpicture_caption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productpicture',
            name='caption',
            field=models.CharField(max_length=120),
        ),
    ]