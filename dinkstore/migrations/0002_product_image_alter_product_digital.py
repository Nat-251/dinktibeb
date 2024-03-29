# Generated by Django 5.0.1 on 2024-01-09 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dinkstore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='digital',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
