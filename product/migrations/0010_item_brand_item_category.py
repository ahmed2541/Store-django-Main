# Generated by Django 4.1.2 on 2022-10-26 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
        ('product', '0009_alter_item_accessories_itaccname'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='settings.brand', verbose_name='Brand'),
        ),
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category', verbose_name='Category'),
        ),
    ]
