# Generated by Django 4.1.4 on 2023-01-12 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_gallerytags_blogtags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogposts',
            name='datePosted',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='galleryposts',
            name='datePosted',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='herosection',
            name='datePosted',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]