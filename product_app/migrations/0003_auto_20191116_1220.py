# Generated by Django 2.2.7 on 2019-11-16 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0002_auto_20191116_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spcategory',
            name='category',
            field=models.CharField(max_length=1000),
        ),
    ]
