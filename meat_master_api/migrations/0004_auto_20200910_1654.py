# Generated by Django 3.1.1 on 2020-09-10 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meat_master_api', '0003_auto_20200905_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='author',
            field=models.CharField(blank=True, default='claytoncanady', max_length=100),
            preserve_default=False,
        ),
    ]
