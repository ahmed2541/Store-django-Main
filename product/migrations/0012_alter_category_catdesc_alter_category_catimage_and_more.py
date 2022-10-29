# Generated by Django 4.1.2 on 2022-10-27 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='CATDesc',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='category',
            name='CATImage',
            field=models.ImageField(blank=True, null=True, upload_to='Images_categories/%y/%m/%d', verbose_name='Category Image'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, default='Images_items/22/10/27/default.png', null=True, upload_to='Images_items/%y/%m/%d', verbose_name='Product image'),
        ),
    ]
