# Generated by Django 4.2.1 on 2023-05-27 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_review_producttag'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default='', upload_to='category_pics'),
            preserve_default=False,
        ),
    ]
