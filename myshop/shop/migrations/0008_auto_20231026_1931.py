# Generated by Django 3.2.22 on 2023-10-26 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_translations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorytranslation',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
