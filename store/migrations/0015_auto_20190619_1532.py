# Generated by Django 2.2.2 on 2019-06-19 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_auto_20190618_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='productCode',
            field=models.CharField(default='--', max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('N/A', 'N/A'), ('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('2XL', '2XL'), ('Small', 'Small (NB)'), ('Large', 'Large (NB)'), ('36', '36'), ('37', '37'), ('38', '38'), ('Male', 'Male'), ('Female', 'Female')], default='N/A', max_length=20),
        ),
    ]
