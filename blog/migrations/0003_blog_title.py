# Generated by Django 4.0.4 on 2022-05-03 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_body_blog_draft'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.CharField(default='', max_length=24),
            preserve_default=False,
        ),
    ]
