# Generated by Django 4.1.2 on 2022-10-26 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_remove_item_image_alter_item_category_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='CATName',
        ),
        migrations.RemoveField(
            model_name='item',
            name='category',
        ),
        migrations.AddField(
            model_name='category',
            name='CATDesc',
            field=models.TextField(default='', verbose_name='Category description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='CATImage',
            field=models.ImageField(default=1, upload_to='Images_categories/%y/%m/%d', verbose_name='Category image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='CATParent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category'),
        ),
    ]