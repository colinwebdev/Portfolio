# Generated by Django 4.1.4 on 2023-01-13 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_alter_blogposts_hastags_alter_galleryposts_hastags_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogPosts',
            new_name='BlogPost',
        ),
        migrations.RenameModel(
            old_name='GalleryTags',
            new_name='BlogTag',
        ),
        migrations.RenameModel(
            old_name='GalleryPosts',
            new_name='GalleryPost',
        ),
        migrations.RenameModel(
            old_name='BlogTags',
            new_name='GalleryTag',
        ),
        migrations.RenameModel(
            old_name='ShopLinks',
            new_name='ShopLink',
        ),
    ]