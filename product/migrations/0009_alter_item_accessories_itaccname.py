# Generated by Django 4.1.2 on 2022-10-26 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_alter_item_accessories_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item_accessories',
            name='ITACCName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Item_Name_ACC', to='product.item', verbose_name='Item'),
        ),
    ]
